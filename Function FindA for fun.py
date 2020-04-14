alist = []
def findA(string):
    for letter in string:
        if letter == 'a' or letter == 'A':
            alist.append(letter)

findA("""Technical Regulations Summary

Fully Assembled Car
Minimum Dimensions = 26 mm
Maximum Dimensions = 34 mm
Total Height = Height between the track and highest point in the car (measured with full 8g CO2 Cartridge
Max Total Height = 65 mm
Total Weight = Weight of car without CO2 Cartridge
Minimum Total Weight = 50 grams
Track Clearance = Distance between the track surface and any part of the car (measured with full 8g CO2 Cartridge
Minimum Track Clearance = 1.5 mm
During the race event, none of the following items may be replaced, added, or replaced during assembly. They have to be fitted on the car already or may be spare/replacement components. Replacements must be identical to those already on the car to be viable.
Rear Wing/Support Structure - Maximum 3
Front Wing/Support Structure and/or nose cone - Maximum 3
Wheel/Wheel Support System - Maximum 3 car sets

Body
For Virtual Cargo, refer to T4.2 and T4.3 of Page 16
The Provided F1 in Schools logo decal must be fully visible from the side of the car and positioned between the front and rear wheels. 
Maximum decal thickness = .5 mm

CO2 Cartridge Chamber
Minimum Diameter of CO2 Cartridge Chamber = 18 mm
Maximum Diameter of CO2 Cartridge Chamber = 18.5 mm
Minimum Distance from rear center of CO2 Cartridge in the car to track surface = 30 mm
Maximum Distance from rear center of CO2 Cartridge in the car to track surface = 40 mm
Minimum Depth of CO2 Cartridge Chamber = 45 mm
Maximum Depth of CO2 Cartridge Chamber = 58 mm
Minimum Angle of CO2 Chamber with full cartridge parallel to track = -3 degrees
Maximum Angle of CO2 Chamber with full cartridge parallel to track = +3 degrees
Minimum thickness of F1 Model Block Material maintained around the minimum chamber volume = 3 mm
Minimum length the CO2 Cartridge protrudes when inserted into the chamber (and fully visible from the top, bottom, and side) = 5 mm
Teatherline Guide
The teather line slot is optional and free in length and location
The teather line guides must be at or 15 mm in front of the front axle centerline, or at or 15 mm behind the back axle centerline
Minimum diameter of teatherline guide = 3.5 mm
Maximum diameter of teatherline guide = 6 mm
The teatherline guide must be robust and completely closed

Wheels and Wheel Support Structures
There must be 2 front wheels and 2 rear wheels which share a common centerline/axis
Minimum distance between closest opposing wheels = 30 mm
Minimum wheel diameter = 26 mm
Maximum wheel diameter = 34 mm 
Minimum width of wheel (excluding fillets) that makes contact with the track = 15 mm
Visibility of wheels must not be obscured by any other part of the car from the top and bottom view. More important info on the actual regulation guide page 22
Visibility of wheels must not be obscured by any part of the car from the side view
Maximum obstruction height from car’s front view of front wheels = 15 mm
Prior to car launch and during the race, all four wheels must touch the track at all times
The wheel diameter must be consistent throughout the entire race
The wheel support system can only be within the area of the cylinder created by (hypothetically) connecting the 2 wheels
The surfaces defining the wheel support structures must be dimensioned and identified by hatching, shading, or block color within the engineering drawings submitted 
The wheels must rotate freely about their own center axis
Minimum distance between the front and rear wheels = 100 mm

Nose Cone
The surfaces defining the nose cone structure must be dimensioned and identified by hatching, shading, or block color within the engineering drawings submitted

Wing and Wing support Structures
Each wing must have a leading edge and trailing edge across its full span
The surfaces defining the front and rear wing support structures must be dimensioned and identified by hatching, shading, or block color within the engineering drawings submitted
Maximum height of everything (front wing, support structures, and nose cone) before the centerline of the front wheel, when viewed from the side = 30 mm
Everything (rear wing and support structures) must be behind the centerline of the rear wheel, when viewed from the side
When viewed from the front, rear wings and front wings may not be obstructed by any part of the car
The total wingspan is the sum of 2 wing segments, each of which must be 25 mm or greater in length
Minimum front wing span = 50 mm
The rear wing is a single, unbroken, piece
Minimum rear wing span = 50 mm
The wing chord (distance between leading and trailing edge chord line measures parallels to the vertical plane) must exist throughout the minimum wingspan. Diagram of wing chord on the actual regulation guide page 27
Minimum length of front wing cord = 1.5 mm
Maximum length of front wing cord = 6 mm
Minimum length of rear wing cord = 1.5 mm
Maximum length of rear wing cord = 6 mm
The wing thickness must exist throughout the wing’s minimum span and at a point along the minimum cord, measures perpendicular to the chord line
Minimum thickness of front wing = 1.5 mm
Maximum thickness of front wing = 6 mm
Minimum thickness of rear wing = 1.5 mm
Maximum thickness of rear wing = 6 mm
Minimum clean “air” space measured from any part of the wings surface to any part of the car or track surface (measured across its minimum span) = 5 mm 
The front wing, rear wing, and any support structure can be manufactured from any separate material but the wing span dimensions must remain the same throughout the race
Only the CO2 Cartridge (positioned by the race officials) is allowed to make contact with the launch pod 
No LERS allowed 
Any car alignment tools must be approved by race officials prior to use



Make sure to add a tether line guide""")
print(alist)

