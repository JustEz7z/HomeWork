def reverse(st):
    st = st.split()
    st.reverse()
    st = " ".join(st)
    return st
reverse("Hello World")
reverse("Hi There.")