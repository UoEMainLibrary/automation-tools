#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple
import importlib
import os
# import shutil

import pytest

dv_pretransfer_module = "transfers.examples.pre-transfer.dataverse"
dataverse = importlib.import_module(dv_pretransfer_module)

# List of dataverse metadata fixtures. We use a namedtuple to provide some
# structure to this index so that we can keep track of information regarding
# dataverse over time, e.g. dataverse version number, the date the dataset was
# created, and so forth.
DataverseMDIndex = namedtuple('DataverseMDIndex',
                              'dv_version created_date title source fname')

dv_1 = DataverseMDIndex("4.8.6",
                        "2016-03-10T14:55:44Z",
                        "Test Dataset",
                        "https://demo.dataverse.org/dataset.xhtml?persistent"
                        "Id=doi:10.5072/FK2/XSAZXH",
                        "demo.dataverse.org.doi.10.5072.1.json")

dv_2 = DataverseMDIndex("4.8.6",
                        "2018-05-16T17:54:01Z",
                        "Bala Parental Alienation Study: Canada, United "
                        "Kingdom, and Australia 1984-2012 [test]",
                        "https://demodv.scholarsportal.info/dataset.xhtml?"
                        "persistentId=doi:10.5072/FK2/UNMEZF",
                        "demo.dataverse.org.doi.10.5072.2.json")

dv_3 = DataverseMDIndex("4.8.6",
                        "2018-05-09T21:26:07Z",
                        "A study with restricted data",
                        "https://demodv.scholarsportal.info/dataset.xhtml?"
                        "persistentId=doi:10.5072/FK2/WZTJWN",
                        "demo.dataverse.org.doi.10.5072.3.json")

dv_4 = DataverseMDIndex("4.8.6",
                        "2018-05-09T20:33:36Z",
                        "A study of my afternoon drinks ",
                        "https://demodv.scholarsportal.info/dataset.xhtml?"
                        "persistentId=doi:10.5072/FK2/6PPJ6Y",
                        "demo.dataverse.org.doi.10.5072.4.json")

dv_5 = DataverseMDIndex("4.8.6",
                        "2018-06-24T20:33:36Z",
                        "A/V and large size files [test]",
                        "https://demodv.scholarsportal.info/dataset.xhtml?"
                        "persistentId=doi:10.5072/FK2/6PPJ6Y",
                        "demo.dataverse.org.doi.10.5072.5.json")

class TestDataverseExample(object):

    write_dir = "fixtures/dataverse/mets/"
    fixture_path = "fixtures/dataverse/"

    @pytest.fixture(autouse=True)
    def setup_session(self):
        try:
            os.makedirs(self.write_dir)
        except FileExistsError:
            # The folder will be removed as part of pytest tear-down following
            # yield.
            pass
        yield
        # TODO: Clear state once the tests have completed...
        # shutil.rmtree(self.write_dir)

    @pytest.mark.parametrize(
        "fixture_path, fixture_name, mets_output_path, mets_name",
        [#(fixture_path, dv_1.fname,
          #write_dir, "METS.{}.xml".format(dv_1.fname)),
         #(fixture_path, dv_2.fname,
         # write_dir, "METS.{}.xml".format(dv_2.fname)),
         #(fixture_path, dv_3.fname,
         # write_dir, "METS.{}.xml".format(dv_3.fname)),
         (fixture_path, dv_4.fname,
          write_dir, "METS.{}.xml".format(dv_4.fname)),
         (fixture_path, dv_5.fname,
          write_dir, "METS.{}.xml".format(dv_5.fname)),
         ])
    def test_parse_dataverse(self,
                             fixture_path,
                             fixture_name,
                             mets_output_path,
                             mets_name):
        dataverse.main(transfer_path=fixture_path,
                       dataset_md_name=fixture_name,
                       md_path=mets_output_path,
                       md_name=mets_name)
