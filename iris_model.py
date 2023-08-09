{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
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
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b45209b-e8bd-434d-b907-9da648e8593e",
   "metadata": {},
   "outputs": [],
   "source": []
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
