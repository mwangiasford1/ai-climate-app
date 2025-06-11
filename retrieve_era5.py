import cdsapi

# Initialize the client
c = cdsapi.Client()

# Request ERA5 data
c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'variable': ['2m_temperature'],
        'year': ['2025'],
        'month': ['06'],
        'day': ['01'],
        'time': ['12:00'],
        'format': 'netcdf',
    },
    'era5_temperature.nc'
)

print("✅ ERA5 data retrieval completed!")
