#!/usr/bin/env python
""" """

# Standard library modules.
import unittest
import logging

# Third party modules.

# Local modules.
from pymontecarlo.testcase import TestCase

from pymontecarlo_casino2.documenthandler import Casino2ProgramDocumentHandler
from pymontecarlo_casino2.program import Casino2Program

# Globals and constants variables.

class TestCasino2ProgramDocumentHandler(TestCase):

    def testconvert(self):
        handler = Casino2ProgramDocumentHandler()
        program = Casino2Program(number_trajectories=500)
        document = self.convert_documenthandler(handler, program)
        self.assertEqual(5, self.count_document_nodes(document))

#        import docutils.core
#        with open('/tmp/test.html', 'wb') as fp:
#            fp.write(docutils.core.publish_from_doctree(document, writer_name='html5'))

if __name__ == '__main__': #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    unittest.main()
