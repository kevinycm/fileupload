#coding=utf-8
__author__ = 'kevin'

import tornado.web
import logging

class UploadHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        status = self.get_argument("status", "")
        logging.error('====================')
        logging.error(status)

        if status == "md5Check":
            md5_encrypt = self.get_argument("md5", "")
            logging.error(md5_encrypt)
        elif status == "chunkCheck":
            name = self.get_argument("name", "")
            chunk_index = self.get_argument("chunkIndex", "")
            size = self.get_argument("size", "")
            logging.error(name)
            logging.error(chunk_index)
            logging.error(size)
        elif status == "chunksMerge":
            name = self.get_argument("name", "")
            chunks = self.get_argument("chunks", "")
            ext = self.get_argument("ext", "")
            md5 = self.get_argument("md5", "")
            logging.error(name)
            logging.error(chunks)
            logging.error(ext)
            logging.error(md5)

        if 'file' in self.request.files:
            files = self.request.files['file']
            for f in files:
                filename = f['filename']
                logging.error('################')
                logging.error(filename)
        self.write("ok")

class DownloadHandler(tornado.web.RequestHandler):
    def get(self):
        pass