
# Adding Plots, PieCharts, and Menus


```bash
text_pub = rospy.Publisher("/text_sample", OverlayText, queue_size=1)
```

```bash
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
text_pub.publish(text)
```



Here you have the complete message:

```bash
rosmsg show jsk_rviz_plugins/OverlayText
uint8 ADD=0
uint8 DELETE=1
uint8 action
int32 width
int32 height
int32 left
int32 top
std_msgs/ColorRGBA bg_color
  float32 r
  float32 g
  float32 b
  float32 a
int32 line_width
float32 text_size
string font
std_msgs/ColorRGBA fg_color
  float32 r
  float32 g
  float32 b
  float32 a
string text
```


# Menu

```bash
menu_publisher = rospy.Publisher("/test_menu", OverlayMenu, queue_size=1)
menu = OverlayMenu()
menu.title = "HaroSystemMode"
menu.menus = ["Sleep", "Searching", "MovingInCircles","Waiting"]
```

Index 1 is Searching

```bash
menu.current_index = 1
menu_publisher.publish(menu)
```


