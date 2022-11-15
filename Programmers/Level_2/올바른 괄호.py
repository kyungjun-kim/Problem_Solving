{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(s):\n",
    "    l,r,num = 0,0,0\n",
    "    if s[0] == \")\" or s[-1] == \"(\" :\n",
    "        return False\n",
    "    for i in s :\n",
    "        if i == \"(\" :\n",
    "            l += 1\n",
    "            num += 1\n",
    "        else :\n",
    "            r += 1\n",
    "            num -= 1\n",
    "        if num < 0 :\n",
    "            #print(num)\n",
    "            return False\n",
    "    if l != r :\n",
    "        return False\n",
    "    return True"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.8.8 ('base')",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "4983dea7fb74a7657ed0a30d17b95d761904bf85c80aa3fbbb72a0182d34178c"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
