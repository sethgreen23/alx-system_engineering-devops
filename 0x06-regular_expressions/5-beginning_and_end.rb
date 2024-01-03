#!/usr/bin/env ruby
#Matching a string that starts with h and end with n
#and can have any string character in between
puts ARGV[0].scan(/^h.n$/).join
