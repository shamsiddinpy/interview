s = "aacecaaa"
for i in range(len(s), 0, -1):
    # Suffix (qoldiq qism) teskari qilib prefixga (oldingi qismga) tengligini tekshiramiz
    if s[i:] == s[i:][::-1]:
        break
        a = s[:i][::-1]
        print(a + s)

        break
