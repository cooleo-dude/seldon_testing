{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a9b934cd-a495-4a25-919d-52383ed7047c",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Model:\n",
    "    def __init__(self):\n",
    "        self._model = pickle.loads( open(\"model.pkl\", \"rb\") )\n",
    "\n",
    "    def predict(self, X):\n",
    "        output = self._model(X)\n",
    "        return output"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
