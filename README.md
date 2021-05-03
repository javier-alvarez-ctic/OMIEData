# OMIEData: 

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI version fury.io](https://img.shields.io/pypi/v/OMIEData.svg)](https://pypi.org/project/OMIEData/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/OMIEData.svg)](https://pypi.python.org/pypi/OMIEData/)

Python package to import data from OMIE (Iberian Peninsula's Electricity Market Operator): https://www.omie.es/

Concretely, you can easily access to data for the following markets:

- Daily market: hourly prices in Spain and Portugal, total hourly energy after auction (with/without billateral contracts), breakdown of the total hourly energy by technology and bid/ask curves.
- Intra-day market: hourly prices for the different sessions and total hourly energy.
- Additional data in next releases.


## Installation 

The package is uploaded at https://pypi.org/project/OMIEData/, so

```python
python -m pip install OMIEData

```
from the command line will install the last version uploaded to pypi. 

Aternatively, to install it from GitHub, type:

```python
python -m pip install git+https://github.com/acruzgarcia/OMIEData

```

in the command line, or use the .whl (or .tar.gz) file within dist (and dist_old) folders as:

```python
python -m pip install OMIEData-VERSION-py3-none-any.whl

```
or

```python
python -m pip install OMIEData-VERSION.tar.gz

```

to install a previous version.

## Examples:

A very simple example to download hourly electricity prices and loads:

```python
dateIni = dt.datetime(2012, 3, 11)
dateEnd = dt.datetime(2012, 4, 15)

# This can take time, it is downloading the files from the website..
df = OMIEMarginalPriceImporter(date_ini=dateIni, date_end=dateEnd).read_to_dataframe(verbose=True)
df.sort_values(by='DATE', axis=0, inplace=True)
print(df)
```

Another example to download hourly loads resulting of the daily market auction, breakdown by technologies:

```python
dateIni = dt.datetime(2020, 6, 1)
dateEnd = dt.datetime(2020, 7, 30)
system_type = SystemType.SPAIN

# This can take time, it is downloading the files from the website..
df = OMIEEnergyByTechnologyImporter(date_ini=dateIni,
                                    date_end=dateEnd,
                                    system_type=system_type).read_to_dataframe(verbose=True)
df.sort_values(by=['DATE', 'HOUR'], axis=0, inplace=True)
print(df)
```


Other examples that illustrate the use of the package:

- [example_energy_by_technology.py](https://github.com/acruzgarcia/OMIEData/blob/dev/examples/example_energy_by_technology_2steps.py)
- [example_marginal_price.py](https://github.com/acruzgarcia/OMIEData/blob/dev/examples/example_marginal_price_2steps.py)

Enjoy!.
