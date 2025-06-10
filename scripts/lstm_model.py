# 🔹 Step 1: Imports
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Bidirectional
from keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import matplotlib.pyplot as plt

# 🔹 Step 2: Generate or Load Data
data = np.sin(np.linspace(0, 100, 1000)).reshape(-1, 1)  # Replace with actual dataset

# 🔹 Step 3: Scale Data
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

# 🔹 Step 4: Create Sequences
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i + seq_length])
        y.append(data[i + seq_length])
    return np.array(X), np.array(y)

sequence_length = 50
X, y = create_sequences(scaled_data, sequence_length)

# 🔹 Step 5: Train-test Split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, shuffle=False)

# 🔹 Step 6: Build LSTM Model
model = Sequential([
    Bidirectional(LSTM(100, activation='tanh', return_sequences=True), input_shape=(X_train.shape[1], 1)),
    Dropout(0.2),
    LSTM(75, activation='tanh'),
    Dense(1)
])

# 🔹 Step 7: Compile Model with Updated Optimizer
model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')

# 🔹 Step 8: Set Up Callbacks
early_stop = EarlyStopping(patience=10, restore_best_weights=True, verbose=1)
checkpoint = ModelCheckpoint('models/best_model.h5', monitor='val_loss', save_best_only=True, verbose=1)

# 🔹 Step 9: Train Model
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_data=(X_val, y_val),
    callbacks=[early_stop, checkpoint],
    verbose=2
)

# 🔹 Step 10: Evaluate Model
loss, mae = model.evaluate(X_val, y_val)
print(f"Test MSE: {loss:.4f}, Test MAE: {mae:.4f}")

# 🔹 Step 11: Training Performance Visualization
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss", linestyle="dashed")
plt.xlabel("Epochs")
plt.ylabel("Loss (MSE)")
plt.title("Model Training & Validation Loss")
plt.legend()
plt.grid(True)
plt.show()