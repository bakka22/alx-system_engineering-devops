#!/usr/bin/env ruby
array = ARGV[0].scan(/((?<=from:).*?.(?=\]))|((?<=to:).*?.(?=\]))|((?<=flags:).*?.(?=\]))/)
array.size.times do |i|
    if i != 0
        print ","
    end
    print array[i][i]
end
print "\n"
