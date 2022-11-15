{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(phone_book):\n",
    "    #phone_book.sort(key = lambda x : len(x))\n",
    "    phone_book.sort()\n",
    "    #print(phone_book)\n",
    "    for i in range(1,len(phone_book)) :\n",
    "        if phone_book[i].startswith(phone_book[i-1]) : \n",
    "            return False\n",
    "    \"\"\"for i in phone_book :\n",
    "        for j in phone_book[phone_book.index(i)+1:] : \n",
    "            if len(i) < len(j) and i == j[:len(i)] :\n",
    "                return False\"\"\"\n",
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
