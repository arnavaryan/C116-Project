import cv2

img= cv2.imread("C:/Users/malho_9yypg6y/Downloads/solar-system.jpg")

text="Sun"

cv2.putText(
    img, 
    "Sun",
    (95,100),
    cv2.FONT_HERSHEY_COMPLEX,
    2,
    (0,0,255)
)

cv2.putText(
    img, 
    "Mercury",
    (65,190),
    cv2.FONT_HERSHEY_COMPLEX,
    0.8,
    (255,255,255)
)
cv2.putText(
    img, 
    "Venus",
    (180,175),
    cv2.FONT_HERSHEY_COMPLEX,
    0.8,
    (255,255,255)
)

cv2.putText(
    img, 
    "Earth",
    (270,175),
    cv2.FONT_HERSHEY_COMPLEX,
    0.8,
    (255,255,255)
)

cv2.putText(
    img, 
    "Mars",
    (375,175),
    cv2.FONT_HERSHEY_COMPLEX,
    0.8,
    (255,255,255)
)

cv2.putText(
    img, 
    "Jupiter",
    (520,60),
    cv2.FONT_HERSHEY_COMPLEX,
    0.8,
    (255,255,255)
)

cv2.putText(
    img, 
    "Saturn",
    (700,125),
    cv2.FONT_HERSHEY_COMPLEX,
    0.8,
    (255,255,255)
)

cv2.putText(
    img, 
    "Uranus",
    (940,125),
    cv2.FONT_HERSHEY_COMPLEX,
    0.8,
    (255,255,255)
)

cv2.putText(
    img, 
    "Neptune",
    (1100,125),
    cv2.FONT_HERSHEY_COMPLEX,
    0.8,
    (255,255,255)
)


cv2.imshow("output",img)

cv2.waitKey(0)