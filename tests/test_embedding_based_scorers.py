# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#


if __name__ == '__main__':
    import unittest
    from tests.scorers import test_bert_score, test_laser

    # initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # add tests to the test suite
    for m in [test_bert_score, test_laser]:
        suite.addTests(loader.loadTestsFromModule(m))

    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
