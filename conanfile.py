#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/stable")

class BoostHanaConan(base.BoostBaseConan):
    name = "boost_hana"
    url = "https://github.com/bincrafters/conan-boost_hana"
    lib_short_names = ["hana"]
    header_only_libs = ["hana"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_fusion",
        "boost_mpl",
        "boost_tuple"
    ]


