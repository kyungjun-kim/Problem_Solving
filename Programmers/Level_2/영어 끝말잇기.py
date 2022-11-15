{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(n, words):\n",
    "    word = words[0][0]\n",
    "    for i,j in enumerate(words) :\n",
    "        if j[0] != word[-1] or words[i] in words[:i]:\n",
    "            return [i%n+1,i//n+1]\n",
    "        word = j\n",
    "    return [0,0]"
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
