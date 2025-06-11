import cdsapi

# Initialize CDS API client
c = cdsapi.Client()

# Download ERA5 climate data
c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'variable': '2m_temperature',
        'year': '2024',
        'month': ['01', '02', '03'],
        'day': ['01', '15'],
        'time': ['00:00', '12:00'],
        'format': 'netcdf',
    },
    'era5_data.nc'
)
