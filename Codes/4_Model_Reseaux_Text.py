{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "4-Model_Reseaux_Text.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPw/xLIfXFwuTVuZF/cV1cx",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/JulienJ-44/rakuteam/blob/main/4_Model_Reseaux_Text.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AxT84Bubh0Wh",
        "outputId": "85d3e55f-5ede-4e40-e00a-cafb9f4523ce"
      },
      "source": [
        "#CONNEXION à google drive\r\n",
        "import pandas as pd\r\n",
        "from google.colab import drive\r\n",
        "\r\n",
        "drive.mount('/Drive')"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Mounted at /Drive\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9swXtIlEuQfK"
      },
      "source": [
        ""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5fXGnjAtnyO3"
      },
      "source": [
        "import matplotlib.pyplot as plt\r\n",
        "plt.style.use('ggplot')\r\n",
        "\r\n",
        "def plot_history(history):\r\n",
        "    acc = history.history['accuracy']\r\n",
        "    val_acc = history.history['val_accuracy']\r\n",
        "    loss = history.history['loss']\r\n",
        "    val_loss = history.history['val_loss']\r\n",
        "    x = range(1, len(acc) + 1)\r\n",
        "\r\n",
        "    plt.figure(figsize=(12, 5))\r\n",
        "    plt.subplot(1, 2, 1)\r\n",
        "    plt.plot(x, acc, 'b', label='Training acc')\r\n",
        "    plt.plot(x, val_acc, 'r', label='Validation acc')\r\n",
        "    plt.title('Training and validation accuracy')\r\n",
        "    plt.legend()\r\n",
        "    plt.subplot(1, 2, 2)\r\n",
        "    plt.plot(x, loss, 'b', label='Training loss')\r\n",
        "    plt.plot(x, val_loss, 'r', label='Validation loss')\r\n",
        "    plt.title('Training and validation loss')\r\n",
        "    plt.legend()"
      ],
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vGx4F4neiDF2",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        },
        "outputId": "7b91dabd-dcfa-4365-8675-8e7b307ea91a"
      },
      "source": [
        "#CHARGEMENT des fichiers\r\n",
        "#dataset_cleaned.csv dot avoir été généré depuis le notebook \"cleaning\"\r\n",
        "import re  \r\n",
        "path = '/Drive/My Drive/Projet Rakuten'\r\n",
        "df = pd.read_csv(f'{path}/dataset_cleaned.csv', index_col=0) \r\n",
        "df = df.replace({'prdtypecode': {10: 1, 2280:2,   50:3, 1280:4, 2705:5, 2522:6, 2582:7, 1560:8, 1281:9, 1920:10, 2403:11,\r\n",
        "       1140:12, 2583:13, 1180:14, 1300:15, 2462:16, 1160:17, 2060:18,   40:19,   60:20, 1320:21, 1302:22,\r\n",
        "       2220:23, 2905:24, 2585:25, 1940:26, 1301:0}})\r\n",
        "#valeurs MANQUANTES\r\n",
        "df['description']=df['description'].fillna(\"\")\r\n",
        "df['designation']=df['designation'].fillna(\"\")\r\n",
        "df=df.replace({'n°': 'numéro '}, regex=True)\r\n",
        "df=df.replace({\"'\": ' '}, regex=True)\r\n",
        "#classes_codes = (y['prdtypecode'].value_counts().index.tolist())\r\n",
        "df.head()"
      ],
      "execution_count": 110,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>designation</th>\n",
              "      <th>description</th>\n",
              "      <th>productid</th>\n",
              "      <th>prdtypecode</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>olivia personalisiertes notizbuch 150 seiten p...</td>\n",
              "      <td></td>\n",
              "      <td>3804725264</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>journal arts numéro  133 28/09/2001 l art marc...</td>\n",
              "      <td></td>\n",
              "      <td>436067568</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>grand stylet ergonomique bleu gamepad nintendo...</td>\n",
              "      <td>pilot style touch pen marque speedlink stylet ...</td>\n",
              "      <td>201115110</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>peluche donald europe disneyland 2000 marionne...</td>\n",
              "      <td></td>\n",
              "      <td>50418756</td>\n",
              "      <td>4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>guerre tuques</td>\n",
              "      <td>luc idées grandeur veut organiser jeu guerre b...</td>\n",
              "      <td>278535884</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                                         designation  ... prdtypecode\n",
              "0  olivia personalisiertes notizbuch 150 seiten p...  ...           1\n",
              "1  journal arts numéro  133 28/09/2001 l art marc...  ...           2\n",
              "2  grand stylet ergonomique bleu gamepad nintendo...  ...           3\n",
              "3  peluche donald europe disneyland 2000 marionne...  ...           4\n",
              "4                                      guerre tuques  ...           5\n",
              "\n",
              "[5 rows x 4 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 110
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EDjqambXiEIY"
      },
      "source": [
        "#on concatène les 2 champs texte\r\n",
        "\r\n",
        "from sklearn.model_selection import train_test_split\r\n",
        "#création dataset train / test \r\n",
        "sentences = df['designation'] + \" \" + df['description']\r\n",
        "y = df['prdtypecode'].values\r\n",
        "#classes_codes = (y['prdtypecode'].value_counts().index.tolist())\r\n"
      ],
      "execution_count": 111,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BSTWHzR24ANk",
        "outputId": "4ce6f955-5ab0-4a6e-a0de-73e06e7420bd"
      },
      "source": [
        "index=1\r\n",
        "print(df['designation'][index])\r\n",
        "print(df['description'][index])\r\n",
        "print(sentences[index])"
      ],
      "execution_count": 107,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "journal arts numéro  133 28/09/2001 l art marche salon d art asiatique paris jacques barrere francois perrier reforme ventes encheres publiques sna fete cent ans\n",
            "\n",
            "journal arts numéro  133 28/09/2001 l art marche salon d art asiatique paris jacques barrere francois perrier reforme ventes encheres publiques sna fete cent ans \n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ycbz_3KkNRQd",
        "outputId": "1ec3f448-0ea2-46e5-86dd-1bbba8d5f82f"
      },
      "source": [
        "pip install git+https://github.com/ClaudeCoulombe/FrenchLefffLemmatizer.git"
      ],
      "execution_count": 92,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Collecting git+https://github.com/ClaudeCoulombe/FrenchLefffLemmatizer.git\n",
            "  Cloning https://github.com/ClaudeCoulombe/FrenchLefffLemmatizer.git to /tmp/pip-req-build-s4fx869y\n",
            "  Running command git clone -q https://github.com/ClaudeCoulombe/FrenchLefffLemmatizer.git /tmp/pip-req-build-s4fx869y\n",
            "Requirement already satisfied (use --upgrade to upgrade): FrenchLefffLemmatizer==0.3 from git+https://github.com/ClaudeCoulombe/FrenchLefffLemmatizer.git in /usr/local/lib/python3.7/dist-packages\n",
            "Building wheels for collected packages: FrenchLefffLemmatizer\n",
            "  Building wheel for FrenchLefffLemmatizer (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for FrenchLefffLemmatizer: filename=FrenchLefffLemmatizer-0.3-cp37-none-any.whl size=3533520 sha256=cbbb48a73856625a348b20984a26e8ca63b0fc5f92adf6d1d68d6c68a4a42e58\n",
            "  Stored in directory: /tmp/pip-ephem-wheel-cache-_3uoz758/wheels/95/b7/c0/e249ca2690c04f6106b9581c5e4111287f71dbd85bac903445\n",
            "Successfully built FrenchLefffLemmatizer\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sWQxc_Ogzyvt",
        "outputId": "35049d04-3b5f-4ff1-8d65-d7c78ee12563"
      },
      "source": [
        "#LEMMATIZATION (OPTIONNAL!! => -1% accuracy)\r\n",
        "print(\"3 premiers articles avant lemmatization\")\r\n",
        "print(sentences[0])\r\n",
        "print(sentences[1])\r\n",
        "print(sentences[2])\r\n",
        "print(sentences[3])\r\n",
        "\r\n",
        "from french_lefff_lemmatizer.french_lefff_lemmatizer import FrenchLefffLemmatizer\r\n",
        "lemmatizer = FrenchLefffLemmatizer()\r\n",
        "#https://github.com/ClaudeCoulombe/FrenchLefffLemmatizer\r\n",
        "\r\n",
        "from nltk.tokenize import word_tokenize\r\n",
        "import nltk as nltk\r\n",
        "nltk.download('punkt') #télécharge les paquets language (dont FR)\r\n",
        "\r\n",
        "def lemmatization(texte):\r\n",
        "  \"\"\"\r\n",
        "  Fonction pour transformer un texte en une suite de mots séparés par des espaces\r\n",
        "  et en excluant les stopwords et les mots de moins de 2 caractères\r\n",
        "  \"\"\"\r\n",
        "  mots = word_tokenize(texte, language='french')\r\n",
        "  tokens = []\r\n",
        "  for mot in mots:\r\n",
        "    if (len(mot)>1):\r\n",
        "      tokens.append(lemmatizer.lemmatize(mot))\r\n",
        "  return tokens\r\n",
        "\r\n",
        "sentences= sentences.apply(lambda x: lemmatization(str(x)))\r\n",
        "print(\"3 premiers articles APRES lemmatization\")\r\n",
        "print(sentences[0])\r\n",
        "print(sentences[1])\r\n",
        "print(sentences[2])\r\n",
        "print(sentences[3])"
      ],
      "execution_count": 109,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "3 premiers articles avant lemmatization\n",
            "olivia personalisiertes notizbuch 150 seiten punktraster ca din a5 rosen-design \n",
            "journal arts numéro  133 28/09/2001 l art marche salon d art asiatique paris jacques barrere francois perrier reforme ventes encheres publiques sna fete cent ans \n",
            "grand stylet ergonomique bleu gamepad nintendo wii speedlink pilot style pilot style touch pen marque speedlink stylet ergonomique gamepad nintendo wii u. confort optimal précision maximale gamepad wii grand stylet hautement ergonomique seulement parfaitement adapté main aussi très élégant livré support fixe sans adhésif l arrière gamepad caractéristiques modèle speedlink pilot style touch pen couleur bleu ref fabricant sl-3468-be compatibilité gamepad nintendo wii forme particulièrement ergonomique excellente tenue main pointe revêtement longue durée conçue abîmer l écran tactile bonus support inclu gamepad\n",
            "peluche donald europe disneyland 2000 marionnette doigt \n",
            "[nltk_data] Downloading package punkt to /root/nltk_data...\n",
            "[nltk_data]   Package punkt is already up-to-date!\n",
            "3 premiers articles APRES lemmatization\n",
            "['olivia', 'personalisiertes', 'notizbuch', '150', 'seiten', 'punktraster', 'ca', 'din', 'a5', 'rosen-design']\n",
            "['journal', 'art', 'numéro', '133', '28/09/2001', 'art', 'marche', 'salon', 'art', 'asiatique', 'pari', 'jacques', 'barrere', 'francois', 'perrier', 'reforme', 'vente', 'encheres', 'publiques', 'sna', 'fete', 'cent', 'an']\n",
            "['grand', 'stylet', 'ergonomique', 'bleu', 'gamepad', 'nintendo', 'wii', 'speedlink', 'pilot', 'style', 'pilot', 'style', 'touch', 'pen', 'marque', 'speedlink', 'stylet', 'ergonomique', 'gamepad', 'nintendo', 'wii', 'u.', 'confort', 'optimal', 'précision', 'maximale', 'gamepad', 'wii', 'grand', 'stylet', 'hautement', 'ergonomique', 'seulement', 'parfaitement', 'adapté', 'main', 'aussi', 'très', 'élégant', 'livré', 'support', 'fixe', 'sans', 'adhésif', 'arrière', 'gamepad', 'caractéristique', 'modèle', 'speedlink', 'pilot', 'style', 'touch', 'pen', 'couleur', 'bleu', 'ref', 'fabricant', 'sl-3468-be', 'compatibilité', 'gamepad', 'nintendo', 'wii', 'forme', 'particulièrement', 'ergonomique', 'excellente', 'tenue', 'main', 'pointe', 'revêtement', 'longue', 'durée', 'conçue', 'abîmer', 'écran', 'tactile', 'bonus', 'support', 'inclu', 'gamepad']\n",
            "['peluche', 'donald', 'europe', 'disneyland', '2000', 'marionnette', 'doigt']\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-N0gd7nn30hF",
        "outputId": "1e20bdab-95fb-4e4f-c38c-8091cf21090e"
      },
      "source": [
        "print(sentences[index])"
      ],
      "execution_count": 103,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "['[', \"'journal\", \"'\", ',', \"'art\", \"'\", ',', \"'numéro\", \"'\", ',', \"'133\", \"'\", ',', \"'28/09/2001\", \"'\", ',', '``', \"l'art\", \"''\", ',', \"'marche\", \"'\", ',', \"'salon\", \"'\", ',', '``', \"d'art\", \"''\", ',', \"'asiatique\", \"'\", ',', \"'pari\", \"'\", ',', \"'jacques\", \"'\", ',', \"'barrere\", \"'\", ',', \"'francois\", \"'\", ',', \"'perrier\", \"'\", ',', \"'reforme\", \"'\", ',', \"'vente\", \"'\", ',', \"'encheres\", \"'\", ',', \"'publiques\", \"'\", ',', \"'sna\", \"'\", ',', \"'fete\", \"'\", ',', \"'cent\", \"'\", ',', \"'an\", \"'\", ']']\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Wdok2tODzzZS"
      },
      "source": [
        "sentences_train, sentences_test, y_train, y_test = train_test_split(\r\n",
        "        sentences, y, test_size=0.2, random_state=123)"
      ],
      "execution_count": 112,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Cbc01DWkpFMO"
      },
      "source": [
        "from keras.utils import np_utils\r\n",
        "y_train = np_utils.to_categorical(y_train, dtype = 'int') # Veiller à n'exécuter cette instruction qu'une seule fois\r\n",
        "y_test = np_utils.to_categorical(y_test, dtype = 'int')   # Veiller à n'exécuter cette instruction qu'une seule fois"
      ],
      "execution_count": 113,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TVawmBeQitWE",
        "outputId": "09eaf868-e557-457c-a9c1-2b80f91141aa"
      },
      "source": [
        "#Création du vocabulaire\r\n",
        "#Tokenization de X_train / X_test et transformation en séquences de mots du vocabulaire\r\n",
        "#   Vocabulary(Keys only) dans tokenizer : [\"'\", \"'cm'\", \"'couleur'\", \"'taille'\", \"'piscine'\", \"'plus'\", \"'peut'\", \"'haute'\", \"'qualité'\", \"'être'\", \"'1\", \"'dimensions'\", ...\r\n",
        "#   Article(texte + description) dans sentences_test/sentences_train: ['jeu', 'chaise', 'longue', 'pcs', 'textilène', 'noir', 'noir']\r\n",
        "#   Représentation de l'article dans X_test/X_train: [21, 288, 435, 494, 5449, 96, 96]\r\n",
        "\r\n",
        "#Note: Pay close attention to the difference between this technique and the X_train that was produced by scikit-learn’s CountVectorizer.\r\n",
        "#With CountVectorizer, we had stacked vectors of word counts, and each vector was the same length (the size of the total corpus vocabulary). \r\n",
        "#With Tokenizer, the resulting vectors equal the length of each text, and the numbers don’t denote counts\r\n",
        "#   , but rather correspond to the word values from the dictionary tokenizer.word_index.\r\n",
        "from keras.preprocessing.text import Tokenizer\r\n",
        "tokenizer = Tokenizer(num_words=20000)#default was 10000/best 20000\r\n",
        "tokenizer.fit_on_texts(sentences_train)\r\n",
        "X_train = tokenizer.texts_to_sequences(sentences_train)\r\n",
        "X_test = tokenizer.texts_to_sequences(sentences_test)\r\n",
        "vocab_size = len(tokenizer.word_index) + 1  # Adding 1 because of reserved 0 index\r\n",
        "print(sentences_train.shape)\r\n",
        "print(len(X_train))\r\n"
      ],
      "execution_count": 114,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "(67932,)\n",
            "67932\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "h-s4qM8gztWg",
        "outputId": "bff47e84-0014-49d6-826b-41b92dae443f"
      },
      "source": [
        "#LONG !!! (optionnal)\r\n",
        "print(f'Vocab : {list(tokenizer.word_index.keys())}')"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "TEST\n",
            " ['jeu', 'chaise', 'longue', 'pcs', 'textilène', 'noir', 'noir'] ['cet', 'ensemble', 'deux', 'chaises', 'longues', 'haute', 'qualité', 'petite', 'table', 'assortie', 'idéal', 'passer', 'après-midi', 'détente', 'jardin', 'camping', 'chaises', 'longues', 'durables', 'faciles', 'nettoyer', 'revêtues', 'textilène', 'doux', 'confortable', 'construites', 'cadre', 'acier', 'robuste', 'deux', 'chaises', 'longues', \"d'extérieur\", 'durables', 'résistants', 'intempéries', \"l'ensemble\", 'complété', 'table', 'assortie', 'élégant', 'dessus', 'table', 'verre', 'lequel', 'pouvez', 'mettre', 'boissons', 'garder', 'livre', 'téléphone', 'portée', 'main', 'cet', 'ensemble', 'excellent', 'ajout', 'espace', 'vie', 'extérieur', 'couleur', 'noir', 'matériau', 'chaise', 'longue', 'structure', 'acier', '43', 'siège', 'dossier', 'textilène', 'dimensions', 'chaise', 'longue', '200', '58', '32', 'cm', 'dimensions', 'table', '30', '30', '295', 'cm', 'hauteur', 'dossier', 'réglable', '62/72/80/89/95', 'cm', 'comprend', 'table', 'dessus', 'table', 'verre', 'mm', \"d'épaisseur\", 'résistance', 'intempéries', 'matériel', 'polyester', '30', 'pvc', '70']\n",
            "TRAIN\n",
            " ['griffes', 'nuit', 'figurine', 'comic', 'book', 'freddy', 'sdcc', '2012'] []\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bJnLJMyxdN4g"
      },
      "source": [
        "#tokenizer.word_index[\"n°\"]=vocab_size"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rPgCtQhy796E",
        "outputId": "145ab07a-8782-4954-ebae-32e6824e1793"
      },
      "source": [
        "tokenizer.word_index[\"numéro\"]"
      ],
      "execution_count": 57,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "59"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 57
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "doN-JZAIi7Gk",
        "outputId": "6a15c2f4-b362-4826-8b9e-6d41bfdee244"
      },
      "source": [
        "#On complète chaque représentation d'article sous la forme [21, 288, 435, 494, 5449, 96, 96] en [21, 288, 435, 494, 5449, 96, 96, 0, 0, 0, ...]\r\n",
        "#pour conserver des tailles de phrases similaires\r\n",
        "from keras.preprocessing.sequence import pad_sequences\r\n",
        "maxlen = 400#defautl was 250, best 400\r\n",
        "X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)\r\n",
        "X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)\r\n",
        "print(len(X_train))"
      ],
      "execution_count": 115,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "67932\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GqO7eD8ijIif",
        "outputId": "b216704e-2f36-4992-e243-0203881d53e4"
      },
      "source": [
        "#DNN1\r\n",
        "from keras.models import Sequential\r\n",
        "from keras import layers\r\n",
        "import keras\r\n",
        "from time import time\r\n",
        "\r\n",
        "t0 = time()\r\n",
        "embedding_dim = 100\r\n",
        "model = Sequential()\r\n",
        "model.add(layers.Embedding(input_dim=vocab_size, \r\n",
        "                           output_dim=embedding_dim, \r\n",
        "                           input_length=maxlen))\r\n",
        "#model.add(layers.GlobalMaxPool1D())\r\n",
        "#model.add(layers.GlobalAveragePooling1D())\r\n",
        "#model.add(Dropout(0.25))\r\n",
        "model.add(layers.Flatten())\r\n",
        "#model.add(layers.Dropout(0.25))\r\n",
        "#model.add(layers.Dense(300, activation='relu'))\r\n",
        "model.add(layers.Dense(100, activation='relu'))\r\n",
        "model.add(layers.Dropout(0.5)) #78.5 sans Dropout; 78.8 avec 0.25; 79.0 avec 0.5;\r\n",
        "model.add(layers.Dense(27, activation='softmax'))\r\n",
        "# last_layer = Dense(units = 27,\r\n",
        "#                      kernel_initializer ='normal',\r\n",
        "#                      activation ='softmax')\r\n",
        "model.compile(optimizer=keras.optimizers.Adam(lr=0.001), #0.001\r\n",
        "              loss='categorical_crossentropy',\r\n",
        "              metrics=['accuracy'])\r\n",
        "model.summary()\r\n",
        "\r\n",
        "history = model.fit(X_train, y_train,\r\n",
        "                    epochs=5,#5\r\n",
        "                    validation_data=(X_test, y_test),\r\n",
        "                    batch_size=200)\r\n",
        "\r\n",
        "print('Time for DNN1: {} mins'.format(round((time() - t0) / 60, 2)))"
      ],
      "execution_count": 117,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Model: \"sequential_11\"\n",
            "_________________________________________________________________\n",
            "Layer (type)                 Output Shape              Param #   \n",
            "=================================================================\n",
            "embedding_11 (Embedding)     (None, 400, 100)          15821900  \n",
            "_________________________________________________________________\n",
            "flatten_8 (Flatten)          (None, 40000)             0         \n",
            "_________________________________________________________________\n",
            "dense_22 (Dense)             (None, 100)               4000100   \n",
            "_________________________________________________________________\n",
            "dropout_6 (Dropout)          (None, 100)               0         \n",
            "_________________________________________________________________\n",
            "dense_23 (Dense)             (None, 27)                2727      \n",
            "=================================================================\n",
            "Total params: 19,824,727\n",
            "Trainable params: 19,824,727\n",
            "Non-trainable params: 0\n",
            "_________________________________________________________________\n",
            "Epoch 1/5\n",
            "340/340 [==============================] - 109s 320ms/step - loss: 2.5709 - accuracy: 0.2710 - val_loss: 0.8184 - val_accuracy: 0.7702\n",
            "Epoch 2/5\n",
            "340/340 [==============================] - 109s 319ms/step - loss: 0.7228 - accuracy: 0.7991 - val_loss: 0.6240 - val_accuracy: 0.8181\n",
            "Epoch 3/5\n",
            "340/340 [==============================] - 107s 315ms/step - loss: 0.4234 - accuracy: 0.8818 - val_loss: 0.6105 - val_accuracy: 0.8240\n",
            "Epoch 4/5\n",
            "340/340 [==============================] - 107s 313ms/step - loss: 0.2903 - accuracy: 0.9204 - val_loss: 0.6312 - val_accuracy: 0.8260\n",
            "Epoch 5/5\n",
            "340/340 [==============================] - 107s 314ms/step - loss: 0.2158 - accuracy: 0.9405 - val_loss: 0.6613 - val_accuracy: 0.8232\n",
            "Time for DNN1: 8.98 mins\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 371
        },
        "id": "T5M4MX_Isl5O",
        "outputId": "6c18c4f6-19ae-43d0-f654-cf5f118f4273"
      },
      "source": [
        "loss, accuracy = model.evaluate(X_train, y_train, verbose=False)\r\n",
        "print(\"Training Accuracy: {:.4f}\".format(accuracy))\r\n",
        "loss, accuracy = model.evaluate(X_test, y_test, verbose=False)\r\n",
        "print(\"Testing Accuracy:  {:.4f}\".format(accuracy))\r\n",
        "plot_history(history)"
      ],
      "execution_count": 90,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Training Accuracy: 0.9738\n",
            "Testing Accuracy:  0.8227\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 864x360 with 2 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e8l9E6Lv-rPT",
        "outputId": "cd4e98de-42e7-4e90-caaa-b9fbf830fc49"
      },
      "source": [
        "y_pred=model.predict(X_test)\r\n",
        "ypred_proba=model.predict_proba(X_test)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/tensorflow/python/keras/engine/sequential.py:425: UserWarning: `model.predict_proba()` is deprecated and will be removed after 2021-01-01. Please use `model.predict()` instead.\n",
            "  warnings.warn('`model.predict_proba()` is deprecated and '\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_VRIak49mnYx"
      },
      "source": [
        "df_tosave=pd.DataFrame(ypred_proba)\r\n",
        "path = '/Drive/My Drive/Projet Rakuten'\r\n",
        "df_tosave.to_csv(f'{path}/ypred_proba_DnnText_score0_82.csv')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 715
        },
        "id": "SW7atrt6jPHQ",
        "outputId": "2d6546f4-87cf-4c8e-bb75-76f40fee8813"
      },
      "source": [
        "#DNN 2\r\n",
        "from keras.models import Sequential\r\n",
        "from keras import layers\r\n",
        "from time import time\r\n",
        "\r\n",
        "t0 = time()\r\n",
        "embedding_dim = 100\r\n",
        "model = Sequential()\r\n",
        "model.add(layers.Embedding(input_dim=vocab_size, \r\n",
        "                           output_dim=embedding_dim, \r\n",
        "                           input_length=maxlen))\r\n",
        "model.add(layers.GlobalMaxPool1D())\r\n",
        "model.add(layers.Dense(100, activation='relu'))\r\n",
        "#model.add(layers.Dense(100, activation='relu'))\r\n",
        "model.add(layers.Dense(27, activation='softmax'))\r\n",
        "model.compile(optimizer=keras.optimizers.Adam(lr=0.001),\r\n",
        "              loss='categorical_crossentropy',\r\n",
        "              metrics=['accuracy'])\r\n",
        "model.summary()\r\n",
        "\r\n",
        "history = model.fit(X_train, y_train,\r\n",
        "                    epochs=5,\r\n",
        "                    #verbose=False,\r\n",
        "                    validation_data=(X_test, y_test),\r\n",
        "                    batch_size=200)\r\n",
        "\r\n",
        "print('Time for DNN2: {} mins'.format(round((time() - t0) / 60, 2)))"
      ],
      "execution_count": 78,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Model: \"sequential_6\"\n",
            "_________________________________________________________________\n",
            "Layer (type)                 Output Shape              Param #   \n",
            "=================================================================\n",
            "embedding_6 (Embedding)      (None, 400, 100)          19695900  \n",
            "_________________________________________________________________\n",
            "global_max_pooling1d_2 (Glob (None, 100)               0         \n",
            "_________________________________________________________________\n",
            "dense_12 (Dense)             (None, 100)               10100     \n",
            "_________________________________________________________________\n",
            "dense_13 (Dense)             (None, 27)                2727      \n",
            "=================================================================\n",
            "Total params: 19,708,727\n",
            "Trainable params: 19,708,727\n",
            "Non-trainable params: 0\n",
            "_________________________________________________________________\n",
            "Epoch 1/5\n",
            "340/340 [==============================] - 90s 263ms/step - loss: 2.6995 - accuracy: 0.2493 - val_loss: 1.1191 - val_accuracy: 0.6962\n",
            "Epoch 2/5\n",
            "174/340 [==============>...............] - ETA: 42s - loss: 0.9701 - accuracy: 0.7302"
          ],
          "name": "stdout"
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-78-1071b92a6891>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     23\u001b[0m                     \u001b[0;31m#verbose=False,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     24\u001b[0m                     \u001b[0mvalidation_data\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mX_test\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my_test\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 25\u001b[0;31m                     batch_size=200)\n\u001b[0m\u001b[1;32m     26\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     27\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Time for DNN2: {} mins'\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mround\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtime\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mt0\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m/\u001b[0m \u001b[0;36m60\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m2\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/tensorflow/python/keras/engine/training.py\u001b[0m in \u001b[0;36mfit\u001b[0;34m(self, x, y, batch_size, epochs, verbose, callbacks, validation_split, validation_data, shuffle, class_weight, sample_weight, initial_epoch, steps_per_epoch, validation_steps, validation_batch_size, validation_freq, max_queue_size, workers, use_multiprocessing)\u001b[0m\n\u001b[1;32m   1098\u001b[0m                 _r=1):\n\u001b[1;32m   1099\u001b[0m               \u001b[0mcallbacks\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mon_train_batch_begin\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mstep\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1100\u001b[0;31m               \u001b[0mtmp_logs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtrain_function\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0miterator\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1101\u001b[0m               \u001b[0;32mif\u001b[0m \u001b[0mdata_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshould_sync\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1102\u001b[0m                 \u001b[0mcontext\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0masync_wait\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/tensorflow/python/eager/def_function.py\u001b[0m in \u001b[0;36m__call__\u001b[0;34m(self, *args, **kwds)\u001b[0m\n\u001b[1;32m    826\u001b[0m     \u001b[0mtracing_count\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexperimental_get_tracing_count\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    827\u001b[0m     \u001b[0;32mwith\u001b[0m \u001b[0mtrace\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mTrace\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_name\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mtm\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 828\u001b[0;31m       \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_call\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    829\u001b[0m       \u001b[0mcompiler\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"xla\"\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_experimental_compile\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0;34m\"nonXla\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    830\u001b[0m       \u001b[0mnew_tracing_count\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexperimental_get_tracing_count\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/tensorflow/python/eager/def_function.py\u001b[0m in \u001b[0;36m_call\u001b[0;34m(self, *args, **kwds)\u001b[0m\n\u001b[1;32m    853\u001b[0m       \u001b[0;31m# In this case we have created variables on the first call, so we run the\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    854\u001b[0m       \u001b[0;31m# defunned version which is guaranteed to never create variables.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 855\u001b[0;31m       \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_stateless_fn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# pylint: disable=not-callable\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    856\u001b[0m     \u001b[0;32melif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_stateful_fn\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    857\u001b[0m       \u001b[0;31m# Release the lock early so that multiple threads can perform the call\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/tensorflow/python/eager/function.py\u001b[0m in \u001b[0;36m__call__\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m   2941\u001b[0m        filtered_flat_args) = self._maybe_define_function(args, kwargs)\n\u001b[1;32m   2942\u001b[0m     return graph_function._call_flat(\n\u001b[0;32m-> 2943\u001b[0;31m         filtered_flat_args, captured_inputs=graph_function.captured_inputs)  # pylint: disable=protected-access\n\u001b[0m\u001b[1;32m   2944\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2945\u001b[0m   \u001b[0;34m@\u001b[0m\u001b[0mproperty\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/tensorflow/python/eager/function.py\u001b[0m in \u001b[0;36m_call_flat\u001b[0;34m(self, args, captured_inputs, cancellation_manager)\u001b[0m\n\u001b[1;32m   1917\u001b[0m       \u001b[0;31m# No tape is watching; skip to running the function.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1918\u001b[0m       return self._build_call_outputs(self._inference_function.call(\n\u001b[0;32m-> 1919\u001b[0;31m           ctx, args, cancellation_manager=cancellation_manager))\n\u001b[0m\u001b[1;32m   1920\u001b[0m     forward_backward = self._select_forward_and_backward_functions(\n\u001b[1;32m   1921\u001b[0m         \u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/tensorflow/python/eager/function.py\u001b[0m in \u001b[0;36mcall\u001b[0;34m(self, ctx, args, cancellation_manager)\u001b[0m\n\u001b[1;32m    558\u001b[0m               \u001b[0minputs\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    559\u001b[0m               \u001b[0mattrs\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mattrs\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 560\u001b[0;31m               ctx=ctx)\n\u001b[0m\u001b[1;32m    561\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    562\u001b[0m           outputs = execute.execute_with_cancellation(\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/tensorflow/python/eager/execute.py\u001b[0m in \u001b[0;36mquick_execute\u001b[0;34m(op_name, num_outputs, inputs, attrs, ctx, name)\u001b[0m\n\u001b[1;32m     58\u001b[0m     \u001b[0mctx\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mensure_initialized\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     59\u001b[0m     tensors = pywrap_tfe.TFE_Py_Execute(ctx._handle, device_name, op_name,\n\u001b[0;32m---> 60\u001b[0;31m                                         inputs, attrs, num_outputs)\n\u001b[0m\u001b[1;32m     61\u001b[0m   \u001b[0;32mexcept\u001b[0m \u001b[0mcore\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_NotOkStatusException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     62\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mname\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "l_jDdql13SWb"
      },
      "source": [
        "#CNN\r\n",
        "from time import time\r\n",
        "\r\n",
        "t0 = time()\r\n",
        "embedding_dim = 100\r\n",
        "\r\n",
        "model = Sequential()\r\n",
        "model.add(layers.Embedding(vocab_size, embedding_dim, input_length=maxlen))\r\n",
        "model.add(layers.Conv1D(128, 3, activation='relu'))\r\n",
        "model.add(layers.GlobalMaxPooling1D())\r\n",
        "model.add(layers.Dense(100, activation='relu'))\r\n",
        "model.add(layers.Dense(27, activation='softmax'))\r\n",
        "model.compile(optimizer=keras.optimizers.Adam(lr=0.001),\r\n",
        "              loss='categorical_crossentropy',\r\n",
        "              metrics=['accuracy'])\r\n",
        "model.summary()\r\n",
        "history = model.fit(X_train, y_train,\r\n",
        "                    epochs=5,\r\n",
        "                    #verbose=False,\r\n",
        "                    validation_data=(X_test, y_test),\r\n",
        "                    batch_size=200)\r\n",
        "\r\n",
        "print('Time for CNN: {} mins'.format(round((time() - t0) / 60, 2)))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hOM6-KXF_-kb"
      },
      "source": [
        "#RNN\r\n",
        "from time import time\r\n",
        "\r\n",
        "t0 = time()\r\n",
        "embedding_dim = 100\r\n",
        "\r\n",
        "model = Sequential()\r\n",
        "model.add(layers.Embedding(vocab_size, embedding_dim, input_length=maxlen))\r\n",
        "model.add(layers.Bidirectional(layers.LSTM(64)))\r\n",
        "model.add(layers.Dense(100, activation='relu'))\r\n",
        "model.add(layers.Dense(27, activation='softmax'))\r\n",
        "model.compile(optimizer=keras.optimizers.Adam(lr=0.001),\r\n",
        "              loss='categorical_crossentropy',\r\n",
        "              metrics=['accuracy'])\r\n",
        "model.summary()\r\n",
        "history = model.fit(X_train, y_train,\r\n",
        "                    epochs=5,\r\n",
        "                    #verbose=False,\r\n",
        "                    validation_data=(X_test, y_test),\r\n",
        "                    batch_size=200)\r\n",
        "\r\n",
        "print('Time for CNN: {} mins'.format(round((time() - t0) / 60, 2)))"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}