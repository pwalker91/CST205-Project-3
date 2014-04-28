def bw():
  pic=pickAFile()
  p=makePicture(pic)
  #show(p)
  height=getHeight(p)
  width=getWidth(p)
  
  for w in range(0, width-1):
    for h in range(0, height-1):
      px = getPixel(p, w, h)
      rcolor = getRed(px)
      gcolor = getGreen(px)
      bcolor = getBlue(px)
      
      average = (rcolor+gcolor+bcolor)/3
      
      if (average > 128):
        setColor(px, black)
      elif (average <=128):
        setColor(px, white)
  
  
  show(p)
  
def grayscale():
  pic=pickAFile()
  p=makePicture(pic)
  #show(p)
  height=getHeight(p)
  width=getWidth(p)
  
  for w in range(0, width-1):
    for h in range(0, height-1):
      px = getPixel(p, w, h)
      level = 255 - int(0.21*getRed(px) + 0.71*getGreen(px) +0.07*getBlue(px))
      color = makeColor(level, level, level)
      setColor(px, color)
      
  show(p)
  
def redGreen():
  pic=pickAFile()
  p=makePicture(pic)
  #show(p)
  height=getHeight(p)
  width=getWidth(p)
  
  for w in range(0, width-1):
    for h in range(0, height-1):
      px = getPixel(p, w, h)
      rcolor = getRed(px)
      gcolor = getGreen(px)
      setRed(px, gcolor)
      setGreen(px, rcolor)
  
  
  show(p)
  
def redBlue():
  pic=pickAFile()
  p=makePicture(pic)
  #show(p)
  height=getHeight(p)
  width=getWidth(p)
  
  for w in range(0, width-1):
    for h in range(0, height-1):
      px = getPixel(p, w, h)
      rcolor = getRed(px)
      bcolor = getBlue(px)
      setRed(px, bcolor)
      setBlue(px, rcolor)
  
  
  show(p)