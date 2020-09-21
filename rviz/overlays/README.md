
```bash
menu_publisher = rospy.Publisher("/test_menu", OverlayMenu, queue_size=1)
menu = OverlayMenu()
menu.title = "HaroSystemMode"
menu.menus = ["Sleep", "Searching", "MovingInCircles","Waiting"]```

# Index 1 is Searching
```bash
menu.current_index = 1
menu_publisher.publish(menu)```
