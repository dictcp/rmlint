#!/usr/bin/env python3
# encoding: utf-8
from tests.utils import *


def test_positive_match_relative_path(usual_setup_usual_teardown):
    create_file('xxx', 'base_a/snap/test')
    create_file('xxx', 'base_b/snap/test')

    head, *data, footer = run_rmlint(
        '--match-relative-path {t}/base_a {t}/base_b'.format(t=TESTDIR_NAME),
        use_default_dir=False
    )
    assert footer['total_files'] == 2
    assert footer['total_lint_size'] == 3
    assert footer['duplicates'] == 1


def test_negative_match_relative_path(usual_setup_usual_teardown):
    create_file('xxx', 'base_a/snap1/test')
    create_file('xxx', 'base_b/snap2/test')

    head, *data, footer = run_rmlint(
        '--match-relative-path {t}/base_a {t}/base_b'.format(t=TESTDIR_NAME),
        use_default_dir=False
    )
    assert footer['total_files'] == 2
    assert footer['total_lint_size'] == 0
    assert footer['duplicates'] == 0


def test_negative_match_relative_path_unequal_depth(usual_setup_usual_teardown):
    create_file('xxx', 'base_a/snap/test')
    create_file('xxx', 'base_b/deeper/snap/test')

    head, *data, footer = run_rmlint(
        '--match-relative-path {t}/base_a {t}/base_b'.format(t=TESTDIR_NAME),
        use_default_dir=False
    )
    assert footer['total_files'] == 2
    assert footer['total_lint_size'] == 0
    assert footer['duplicates'] == 0


def test_positive_match_relative_path_depth_4(usual_setup_usual_teardown):
    create_file('xxx', 'base_a/l1/l2/l3/test')
    create_file('xxx', 'base_b/l1/l2/l3/test')

    head, *data, footer = run_rmlint(
        '--match-relative-path {t}/base_a {t}/base_b'.format(t=TESTDIR_NAME),
        use_default_dir=False
    )
    assert footer['total_files'] == 2
    assert footer['total_lint_size'] == 3
    assert footer['duplicates'] == 1
