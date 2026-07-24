import razorpay


RAZORPAY_KEY_ID = "rzp_test_THLChksOcjNFxu"

RAZORPAY_KEY_SECRET = "cePcvdHAz5MrxtONRYrv61Vh"



client = razorpay.Client(
    auth=(
        RAZORPAY_KEY_ID,
        RAZORPAY_KEY_SECRET
    )
)