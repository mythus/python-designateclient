"""
Copyright 2015 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import random
import string


def random_digits(n=8):
    return "".join([random.choice(string.digits) for _ in range(n)])


def random_tld(name='testtld'):
    return "{0}{1}".format(name, random_digits())


def random_zone_name(name='testdomain', tld='com'):
    return "{0}{1}.{2}.".format(name, random_digits(), tld)


def random_a_recordset_name(zone_name, recordset_name='testrecord'):
    return "{0}{1}.{2}".format(recordset_name, random_digits(), zone_name)
