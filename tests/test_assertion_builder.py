## #!/usr/bin/env python
# -*- coding: utf-8 -*-
# <sure - assertion toolbox>
# Copyright (C) <2010-2012>  Gabriel Falcão <gabriel@nacaolivre.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from sure import this, these, those, it, that, AssertionBuilder


def test_assertion_builder_synonyms():
    (u"this, it, these and those are all synonyms")

    assert that(it).is_a(AssertionBuilder)
    assert that(this).is_a(AssertionBuilder)
    assert that(these).is_a(AssertionBuilder)
    assert that(those).is_a(AssertionBuilder)


def test_4_2p2():
    (u"this(4).should.equal(2 + 2)")

    assert this(4).should.equal(2 + 2)

    def opposite():
        assert this(4).should.equal(8)

    assert that(opposite).raises(AssertionError)
    assert that(opposite).raises("X is 4 whereas Y is 8")