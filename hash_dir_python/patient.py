import json
import sys

class patient:
    def __init__(self, filename, hash, analysis):
        self.filename = filename
        self.hash = hash
        self.analysis = analysis
