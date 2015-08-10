import os, eyed3

folder = raw_input("Directory of Files:/>") 
for root, dirs, filenames in os.walk(folder):
    tracks = 0
    for filename in filenames:
		
		print "opening",filename  
		try:
			tracknr = int(filename[0:2])

		except:
			print "not in the right format"
			print """they should be like this
					01.mp3 02somename.mp3 
					not a1.mp3 or 1asomename.mp3
					this can be easily modified
					change the tracknr var into
					the place you want it to grab
					the number from [#]_[#]"""
		try: 
			audiofile = eyed3.load(folder+"/"+filename)
			
			audiofile.tag.track_num = tracknr 
			
			audiofile.tag.save()
			tracks += 1			
			print "Track number appended to  %s %d" % (filename,tracks)
		except:
			print "not an mp3 muble"
			print ("this is not " +filename)
        	
  
  
