#!/usr/bin/env ruby

ORDER = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`|~ \n"

def enc_string(str)
  str.chars.map {|c|
    (33 + ORDER.index(c)).chr
  }.join
end

def rle(text)
  rle_data = []

  last = nil
  cnt = 0
  text.chars.each_slice(1) do |chunk|
    txt = chunk.join
    if (cnt < 22 && txt == last) || last == nil
      cnt += 1
      last = txt
    else
      rle_data << [last, cnt]
      cnt = 1
      last = txt
    end
  end

  rle_data << [last, cnt]

  buf = []
  rle_data.reverse_each do |txt, cnt|
    ord = "UDLR".index(txt)
    # buf << enc_string(txt) + (cnt + 33).chr
    buf << (ord + cnt * 4 + 33).chr
  end

  buf.join
end

puts rle(ARGF.read.chomp)
