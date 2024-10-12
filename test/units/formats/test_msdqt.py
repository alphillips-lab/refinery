#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .. import TestUnitBase
from hashlib import sha256


class TestMSDQT(TestUnitBase):

    def test_unquarantine(self):
        data = self.download_sample('72282c79844f7d5f31b05571cadd14e4d32c55aef82d12d43aa70825d66ea2e6')
        extracted = data | self.load() | ...
        self.assertEquals(sha256(extracted).hexdigest().lower(),
            "8780cf5af7e12a03884893de39c035849ec319eab0fc332e06d47390b9590b41")
