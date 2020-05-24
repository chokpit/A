# Compare md5 checksums from source (A) and destination (B)

with open('md5_source.txt', 'r') as fsource:
  source = fsource.read()

with open('md5_from_destination.txt', 'r') as fdest:
  destination = fdest.read()


if source == destination:
	print 'The file has been sent successfully, md5 checksums are equals'
else:
	print 'The file has been sent unsuccessfully, md5 checksums are not equals'
