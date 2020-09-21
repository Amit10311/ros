
```bash

text_pub = rospy.Publisher("/text_sample", OverlayText, queue_size=1)

text = OverlayText()

text.width = 200
text.height = 400
text.left = 10
text.top = 10
text.text_size = 12
text.line_width = 2
text.font = "DejaVu Sans Mono"
text.text = """Distance=  %s.
Angle=%s.
Counter = <span style="color: green;">%d.</span>
""" % (str(number), str(number2) ,self.counter)
text.fg_color = ColorRGBA(25 / 255.0, 1.0, 240.0 / 255.0, 1.0)
text.bg_color = ColorRGBA(0.0, 0.0, 0.0, 0.2)

text_pub.publish(text)```

```bash
menu_publisher = rospy.Publisher("/test_menu", OverlayMenu, queue_size=1)
menu = OverlayMenu()
menu.title = "HaroSystemMode"
menu.menus = ["Sleep", "Searching", "MovingInCircles","Waiting"]```

# Index 1 is Searching
```bash
menu.current_index = 1
menu_publisher.publish(menu)```

