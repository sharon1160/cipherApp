################# PRINT #################

def printHeader(matrixHeader):
  msg = ''
  for k in matrixHeader:
    msg += matrixHeader[k] + ' '
  msg += '\n'
  for k in matrixHeader:
    msg += str(k) + ' '
  msg += '\n'
  return msg

def printMatrix(matrix):
  msg = ''
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      msg += matrix[i][j] + " "
    msg += '\n'
  msg += '\n'
  return msg

################# PRE-PROCESSING #################

def removeAccents(text):
  vowelReplacements = [
    ('á','a'),
    ('é','e'),
    ('í','i'),
    ('ó','o'),
    ('ú','u')
  ]
  for a1, a2 in vowelReplacements:
    text = text.replace(a1, a2)
  return text

def removeSpacesSigns(text):
  punctuationMarks = [',',';',':','¿','?','!','¡','.']
  for item in punctuationMarks:
    text = text.replace(item,'')
  text = text.replace(' ','').replace('\n','')
  return text

def preprocess(text):
  text = removeSpacesSigns(text)
  text = removeAccents(text)
  text = text.replace('ñ','n')
  text = text.upper()
  return text

################# HEAD MATRIX #################

def sortKey (clave):
  clave = ''.join(sorted(clave))
  orderedKey = list(clave)
  return orderedKey

def generateHeader(key, orderedKey):
  matrixHeader = {}
  for i in range(len(orderedKey)):
    pos = orderedKey.index(key[i])
    matrixHeader[pos + 1] = key[i]
    orderedKey[pos] = "-"
  return matrixHeader

################# TRANSPOSITION INTERRUPTED #################

def getEncryptedText(matrixHeader, matrix):
  result = ""
  for col in range(len(matrixHeader)):
    colMatrix = list(matrixHeader).index(col+1)
    for row in matrix:
      result += row[colMatrix]
    result += " "
  return result

def interruptedTransposition(key, text):
  # Key and plain text preprocessing
  key = preprocess(key)
  text = preprocess(text)

  # HEAD
  orderedKey = sortKey(key)
  matrixHeader = generateHeader(key, orderedKey)

  # MATRIX
  matrix = []
  flag = False 

  i = 0 # Preprocessed text index 
  numrow = 0 # Variable that stores the row number

  while flag == False:

    row = [""] * len(matrixHeader) # Row
    f = 0 # Index of the created row

    for key in matrixHeader:

      # If all the preprocessed text has been read, break the two loops
      if i >= len(text):
        flag = True
        break

      # If the row number matches the column key,
      # break the loop and go to the next row
      if (numrow + 1) == key:
        row[f] += text[i]
        f += 1
        i += 1
        break
      else:
        row[f] += text[i]
        f += 1
        i += 1

    numrow += 1
    matrix.append(row)

  # GET ENCRYPTED TEXT
  result = getEncryptedText(matrixHeader, matrix)

  # GET MATRIX
  msg = ""
  msg += printHeader(matrixHeader)
  msg += "----------------------------\n"
  msg += printMatrix(matrix)
  return result, msg

