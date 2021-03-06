import unittest

import add_test
import circle_test
import count_test
import fix_csv_test
import parse_ranges_test
import point_test
import tail_test


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(circle_test.CircleTests))
    suite.addTest(unittest.makeSuite(count_test.CountWordsTests))
    suite.addTest(unittest.makeSuite(add_test.AddTests))
    suite.addTest(unittest.makeSuite(tail_test.TailTests))
    suite.addTest(unittest.makeSuite(parse_ranges_test.ParseRangesTests))
    suite.addTest(unittest.makeSuite(point_test.PointTests))
    suite.addTest(unittest.makeSuite(fix_csv_test.FixCSVTests))
    return suite


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""

    class resultclass(unittest.TextTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    import sys
    from platform import python_version

    if sys.version_info < (3, 6):
        sys.exit("Running {}.  Python 3.6 required.".format(python_version()))
    mysuite = suite()
    runner = AllowUnexpectedSuccessRunner()
    runner.run(mysuite)
