{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "**Loading Data**"
      ],
      "metadata": {
        "id": "TGzTgmtr_bB-"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3n6zxOJw8aKD",
        "outputId": "be91a368-1f19-45c4-9bf0-8f7968e0d4aa"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "District Data:\n",
            "   OBJECTID     NAME     POP        Area  S_Yield_Ha  M_Yield_Ha  \\\n",
            "0        92     ABIM   90385  2771977106         449        1040   \n",
            "1        96   AMUDAT  101790  1643582836         205        1297   \n",
            "2        20  KAABONG  627057  7373606003         279         945   \n",
            "3        85   KOTIDO  243157  3641539808         331        1148   \n",
            "4         5   MOROTO  127811  3570160948         128         355   \n",
            "\n",
            "   Crop_Area_Ha     S_Area_Ha    M_Area_Ha  S_Prod_Tot  M_Prod_Tot  \n",
            "0   5470.068394   3277.295971  1848.621855     1471506     1922567  \n",
            "1   5765.443719   2973.423860  2733.661014      609552     3545558  \n",
            "2  28121.672530  20544.194960  7394.416334     5731830     6987723  \n",
            "3  53032.649450  50247.443900  1751.372284    16631904     2010575  \n",
            "4   5954.814048   4741.748776  1190.050606      606944      422468  \n",
            "\n",
            "Subcounty Data:\n",
            "   OBJECTID       SUBCOUNTY_NAME DISTRICT_NAME    POP        Area Karamoja  \\\n",
            "0       263              KACHERI        KOTIDO  17244  1067176155        Y   \n",
            "1       264               KOTIDO        KOTIDO  52771   597575188        Y   \n",
            "2       265  KOTIDO TOWN COUNCIL        KOTIDO  27389    23972401        Y   \n",
            "3       266         NAKAPERIMORU        KOTIDO  38775   419111591        Y   \n",
            "4       267           PANYANGARA        KOTIDO  65704   880955930        Y   \n",
            "\n",
            "   S_Yield_Ha   M_Yield_Ha  Crop_Area_Ha     S_Area_Ha   M_Area_Ha  \\\n",
            "0  354.207411  1137.467019   7023.533691   6434.342449  528.124229   \n",
            "1  367.890523  1162.996687  13587.990760  12455.592640  824.767081   \n",
            "2  369.314177  1167.005832   1656.531855   1520.322052    8.561644   \n",
            "3  283.324569   852.366578   7087.823334   6761.488901   45.721712   \n",
            "4  373.836926  1283.859882  10398.249390  10111.198130  172.611914   \n",
            "\n",
            "     S_Prod_Tot     M_Prod_Tot  \n",
            "0  2.279092e+06  600723.892900  \n",
            "1  4.582294e+06  959201.382500  \n",
            "2  5.614765e+05    9991.488268  \n",
            "3  1.915696e+06   38971.659080  \n",
            "4  3.779939e+06  221609.511400  \n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "\n",
        "# Load the district-level data\n",
        "district_data = pd.read_csv('/content/Uganda_Karamoja_District_Crop_Yield_Population.csv')\n",
        "\n",
        "# Load the subcounty-level data\n",
        "subcounty_data = pd.read_csv('/content/Uganda_Karamoja_Subcounty_Crop_Yield_Population.csv')\n",
        "\n",
        "# Display the first few rows\n",
        "print(\"District Data:\")\n",
        "print(district_data.head())\n",
        "\n",
        "print(\"\\nSubcounty Data:\")\n",
        "print(subcounty_data.head())\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Data Inspection**"
      ],
      "metadata": {
        "id": "AUS0T6Ta_XZQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Check for missing values\n",
        "print(\"Missing values in district data:\")\n",
        "print(district_data.isnull().sum())\n",
        "\n",
        "print(\"\\nMissing values in subcounty data:\")\n",
        "print(subcounty_data.isnull().sum())\n",
        "\n",
        "# Check for duplicates\n",
        "print(\"\\nDuplicates in district data:\", district_data.duplicated().sum())\n",
        "print(\"Duplicates in subcounty data:\", subcounty_data.duplicated().sum())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nA21S-vs-Y9e",
        "outputId": "cdcffa57-4df7-43f9-98c0-c8cc47b40bae"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Missing values in district data:\n",
            "OBJECTID        0\n",
            "NAME            0\n",
            "POP             0\n",
            "Area            0\n",
            "S_Yield_Ha      0\n",
            "M_Yield_Ha      0\n",
            "Crop_Area_Ha    0\n",
            "S_Area_Ha       0\n",
            "M_Area_Ha       0\n",
            "S_Prod_Tot      0\n",
            "M_Prod_Tot      0\n",
            "dtype: int64\n",
            "\n",
            "Missing values in subcounty data:\n",
            "OBJECTID          0\n",
            "SUBCOUNTY_NAME    0\n",
            "DISTRICT_NAME     0\n",
            "POP               0\n",
            "Area              0\n",
            "Karamoja          0\n",
            "S_Yield_Ha        0\n",
            "M_Yield_Ha        0\n",
            "Crop_Area_Ha      0\n",
            "S_Area_Ha         0\n",
            "M_Area_Ha         0\n",
            "S_Prod_Tot        0\n",
            "M_Prod_Tot        0\n",
            "dtype: int64\n",
            "\n",
            "Duplicates in district data: 0\n",
            "Duplicates in subcounty data: 0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Data Cleaning**"
      ],
      "metadata": {
        "id": "857U52hF_ULF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Convert the 'Karamoja' column to boolean\n",
        "subcounty_data['Karamoja'] = subcounty_data['Karamoja'].apply(lambda x: True if x == 'Y' else False)\n",
        "\n",
        "# Check the changes to ensure the conversion was successful\n",
        "print(subcounty_data[['SUBCOUNTY_NAME', 'DISTRICT_NAME', 'Karamoja']].head())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "C63BCIPl-fNn",
        "outputId": "f0603ed4-7cd7-46c8-bcb1-a17b5c62d4b3"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "        SUBCOUNTY_NAME DISTRICT_NAME  Karamoja\n",
            "0              KACHERI        KOTIDO      True\n",
            "1               KOTIDO        KOTIDO      True\n",
            "2  KOTIDO TOWN COUNCIL        KOTIDO      True\n",
            "3         NAKAPERIMORU        KOTIDO      True\n",
            "4           PANYANGARA        KOTIDO      True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Data Merging**"
      ],
      "metadata": {
        "id": "ehvyPHBJ_fiO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Merge the subcounty data with district data on the 'DISTRICT_NAME' field\n",
        "merged_data = pd.merge(subcounty_data, district_data, left_on='DISTRICT_NAME', right_on='NAME', suffixes=('_subcounty', '_district'))\n",
        "\n",
        "# Display the first few rows\n",
        "print(\"Merged Data:\")\n",
        "print(merged_data.head())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4nW1xDoz_ht4",
        "outputId": "56ce25b5-2246-4e0a-bfaa-ad799de13dcc"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Merged Data:\n",
            "   OBJECTID_subcounty       SUBCOUNTY_NAME DISTRICT_NAME  POP_subcounty  \\\n",
            "0                 263              KACHERI        KOTIDO          17244   \n",
            "1                 264               KOTIDO        KOTIDO          52771   \n",
            "2                 265  KOTIDO TOWN COUNCIL        KOTIDO          27389   \n",
            "3                 266         NAKAPERIMORU        KOTIDO          38775   \n",
            "4                 267           PANYANGARA        KOTIDO          65704   \n",
            "\n",
            "   Area_subcounty  Karamoja  S_Yield_Ha_subcounty  M_Yield_Ha_subcounty  \\\n",
            "0      1067176155      True            354.207411           1137.467019   \n",
            "1       597575188      True            367.890523           1162.996687   \n",
            "2        23972401      True            369.314177           1167.005832   \n",
            "3       419111591      True            283.324569            852.366578   \n",
            "4       880955930      True            373.836926           1283.859882   \n",
            "\n",
            "   Crop_Area_Ha_subcounty  S_Area_Ha_subcounty  ...    NAME  POP_district  \\\n",
            "0             7023.533691          6434.342449  ...  KOTIDO        243157   \n",
            "1            13587.990760         12455.592640  ...  KOTIDO        243157   \n",
            "2             1656.531855          1520.322052  ...  KOTIDO        243157   \n",
            "3             7087.823334          6761.488901  ...  KOTIDO        243157   \n",
            "4            10398.249390         10111.198130  ...  KOTIDO        243157   \n",
            "\n",
            "   Area_district  S_Yield_Ha_district M_Yield_Ha_district  \\\n",
            "0     3641539808                  331                1148   \n",
            "1     3641539808                  331                1148   \n",
            "2     3641539808                  331                1148   \n",
            "3     3641539808                  331                1148   \n",
            "4     3641539808                  331                1148   \n",
            "\n",
            "   Crop_Area_Ha_district  S_Area_Ha_district  M_Area_Ha_district  \\\n",
            "0            53032.64945          50247.4439         1751.372284   \n",
            "1            53032.64945          50247.4439         1751.372284   \n",
            "2            53032.64945          50247.4439         1751.372284   \n",
            "3            53032.64945          50247.4439         1751.372284   \n",
            "4            53032.64945          50247.4439         1751.372284   \n",
            "\n",
            "   S_Prod_Tot_district  M_Prod_Tot_district  \n",
            "0             16631904              2010575  \n",
            "1             16631904              2010575  \n",
            "2             16631904              2010575  \n",
            "3             16631904              2010575  \n",
            "4             16631904              2010575  \n",
            "\n",
            "[5 rows x 24 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Remove Redundant Columns**"
      ],
      "metadata": {
        "id": "t9YQzfCA_2ot"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "merged_data.drop(columns=['NAME'], inplace=True)\n"
      ],
      "metadata": {
        "id": "oRh5Mg4C_3nH"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Saving the data**"
      ],
      "metadata": {
        "id": "wE-QcQ0OAldu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Save the merged data\n",
        "merged_data.to_csv('Merged_Karamoja_Crop_Yield_Population.csv', index=False)\n"
      ],
      "metadata": {
        "id": "jXww3aF3AnmO"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "\n",
        "# Download the file to my computer\n",
        "files.download('Merged_Karamoja_Crop_Yield_Population.csv')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 17
        },
        "id": "sxhuHn4WAv7l",
        "outputId": "423dab03-5459-496c-ce9f-44f614875495"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_61f45ae9-3000-4e4a-ab38-2142032b83cf\", \"Merged_Karamoja_Crop_Yield_Population.csv\", 11186)"
            ]
          },
          "metadata": {}
        }
      ]
    }
  ]
}

print("Processing complete. Cleaned data saved successfully!")