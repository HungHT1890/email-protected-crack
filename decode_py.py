import urllib.parse
def decode_email(encoded_email):
    email = ""
    key = int(encoded_email[:2], 16)
    # hàm int ngoài dùng để ép kiểu - xác định kiểu dữ liệu - còn được dùng để chuyển giá trị từ một hệ cơ số khác sang hệ cơ số 10
    # > ví dụ 50 hệ 16 sang hệ 10 => 5 * 16 + 0*1 => 80 (vậy sang hệ 10 thì số 50 của hệ 16 sẽ là 80)
    # key được xác định là hai kí tự đầu của chuỗi , 16 là cách để chuyển nó sang dạng hex vì hex là hệ cơ số 16
    for i in range(2, len(encoded_email), 2):
        """
        - tại sao lại lấy giá trị bắt đầu từ index 2 => vì 2 kí tự đầu được xác định là key của đoạn mã hóa
        - tại sao lại lấy giá trị với bước nhảy là 2 => vì 2 kí tự tiếp theo được xác định là kí tự tiếp theo
        - i lấy từ i , i + 2 lấy từ i đến khoảng i + 2 => nếu i bằng 2 lấy đơn thuần chỉ có thể lấy được 1 kí tự => xác định khoảng của 2 kí tự => 2 + 2 => khoảng sẽ là [2:4]
        - int(encoded_email[i:i+2]) => chuyển đổi kí tự hex sang dạng số nguyên => hệ cơ hố 16 sang hệ 10
        - ^key => với key đã được xử dụng để mã hóa => sử dụng nó để thực hiện thuật toán XOR
        - char() => sử dụng hàm char để tìm kí tự tương ứng trong bảng mã unicode (phạm vi 0 - 1.114,111)
        """
        encode_value = encoded_email[i:i+2] # key
        value_16_to_10  = int(str(encode_value),16) # chuyển đổi hệ 16 sang 10 => mặc định của int() là hệ 10 decimal
        char_code = value_16_to_10 ^ key
        email += chr(char_code) # lấy ra kí tự sau đó += mail ban đầu
    try:
        # unquote email => không sử dụng vẫn ổn - nhưng cho vào cho đủ trường hợp
        email = urllib.parse.unquote(email)
    except Exception as e:
        print(e)
    return email
if __name__ == '__main__':
    email_encode = '48203d262f3b2923217a78787b082f25292124662b2725'
    email = decode_email(email_encode)
    print(email)
    
