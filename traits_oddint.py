# -*- coding:utf-8 -*-
from enthought.traits.api import *

class OddInt(BaseInt):

    # 定义默认值
    default_value = 1

    # tratis类型的描述文字
    info_text = 'an odd integer'

    def validate(self, object, name, value):
        "校验值是否为奇数"
        value = super(OddInt, self).validate(object, name, value)
        if (value % 2) == 1:
            return value

        self.error(object, name, value)
