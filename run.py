#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     run.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.07.31   21:42
-------------------------------------------------------------------------------
   @Change:   2020.07.31
-------------------------------------------------------------------------------
"""
import re

from apps.app import create_app
from config import Config

app = create_app()


@app.template_filter('summary')
def summary(data):
    pattern = r'</?[?a-zA-Z]+[^><]*>|&[a-zA-Z]{1,10};'
    return re.sub(pattern, ' ', data).strip()


if __name__ == "__main__":
    app.run(debug=Config.DEBUG)
