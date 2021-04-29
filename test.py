# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 14:11:31 2021

@author: User
"""
import jobmetadatalogger
import json

fmdu = jobmetadatalogger.FileMetaDataUpdate()
fmdu.fileName = "12345678910"
fmdu.batch_id = "Foo"
fmdu.status = "started"
fmdu.job_details = "Publishorama"
fmdu.save()

jobmetadatalogger.is_file_processed(self.fileName)

