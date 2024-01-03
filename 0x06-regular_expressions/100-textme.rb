#!/usr/bin/env ruby
#Matching a string that starts with h and end with n
#and can have any string character in between
matches = ARGV[0].scan(/.*from:([\w\+]+)\].*to:([\w\+]+)\].*flags:([\w\+\-\:]+).*/)
if matches.any?
  timestamp, sender, message = matches[0]
  puts "#{timestamp},#{sender},#{message}"
end
