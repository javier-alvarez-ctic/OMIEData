import pandas as pd
import datetime as dt

from OMIEData.DataImport.omie_data_importer import OMIEDataImporter
from OMIEData.FileReaders.omie_file_reader import OMIEFileReader
from OMIEData.Downloaders.omie_downloader import OMIEDownloader


class OMIEDataImporterFromResponses(OMIEDataImporter):

    def __init__(self,
                 date_ini: dt.date,
                 date_end: dt.date,
                 file_downloader: OMIEDownloader,
                 file_reader: OMIEFileReader):

        self.fileDownloader = file_downloader
        self.fileReader = file_reader
        self.date_ini = date_ini
        self.date_end = date_end

    def read_to_dataframe(self, verbose=False) -> pd.DataFrame:

        df = pd.DataFrame(columns=self.fileReader.get_keys())
        for response in self.fileDownloader.url_responses(date_ini=self.date_ini,
                                                          date_end=self.date_end,
                                                          verbose=verbose):
            try:
                df = pd.concat([df, self.fileReader.get_data_from_response(response=response)],ignore_index=True)

            except Exception as exc:
                print('There was error processing file: ' + response.url)
                print('{}'.format(exc) + response.url)
            else:
                if verbose:
                    print('Url: ' + response.url + ' successfully processed')

        return df
