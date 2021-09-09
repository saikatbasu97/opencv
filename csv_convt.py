
my_list= [('12PM_to_1PM', (570, 375), (48, 53)), ('1PM_to_2PM', (542, 456), (46, 64)), ('1PM_to_2PM', (550, 445), (47, 63)), ('1PM_to_2PM', (557, 429), (47, 60)), ('1PM_to_2PM', (562, 419), (48, 59)), ('1PM_to_2PM', (567, 409), (48, 58)), ('3PM_to_4PM', (469, 523), (40, 74)), ('3PM_to_4PM', (484, 517), (41, 73)), ('3PM_to_4PM', (495, 508), (42, 72)), ('4PM_to_5PM', (416, 545), (35, 77)), ('4PM_to_5PM', (430, 540), (36, 76)), ('4PM_to_5PM', (445, 536), (38, 76)), ('5PM_to_6PM', (352, 552), (30, 78)), ('6PM_to_7PM', (316, 541), (27, 76)), ('6PM_to_7PM', (306, 536), (26, 76)), ('7PM_to_8PM', (268, 520), (22, 73)), ('8PM_to_9PM', (253, 513), (21, 72)), ('8PM_to_9PM', (239, 506), (20, 71)), ('8PM_to_9PM', (220, 496), (18, 70)), ('9PM_to_10PM', (209, 489), (17, 69)), ('9PM_to_10PM', (199, 481), (17, 68)), ('9PM_to_10PM', (189, 470), (16, 66)), ('10PM_to_11PM', (168, 437), (14, 62)), ('10PM_to_11PM', (162, 425), (13, 60)), ('10PM_to_11PM', (156, 412), (13, 58)), ('11PM_to_12AM', (150, 400), (12, 56)), ('11PM_to_12AM', (147, 388), (12, 55)), ('11PM_to_12AM', (142, 350), (12, 49)), ('12AM_to_1AM', (142, 350), (12, 49)), ('12AM_to_1AM', (146, 310), (12, 44)), ('12AM_to_1AM', (149, 298), (12, 42)), ('1AM_to_2AM', (159, 275), (13, 39)), ('1AM_to_2AM', (165, 259), (14, 36)), ('2AM_to_3AM', (170, 235), (14, 33)), ('2AM_to_3AM', (186, 229), (15, 32)), ('2AM_to_3AM', (203, 209), (17, 29)), ('3AM_to_4AM', (213, 200), (18, 28)), ('3AM_to_4AM', (246, 174), (21, 24)), ('4AM_to_5AM', (294, 158), (25, 22)), ('5AM_to_6AM', (337, 152), (28, 21)), ('5AM_to_6AM', (349, 151), (29, 21)), ('6AM_to_7AM', (389, 152), (33, 21)), ('7AM_to_8AM', (442, 165), (37, 23)), ('7AM_to_8AM', (429, 160), (36, 22)), ('7AM_to_8AM', (415, 157), (35, 22)), ('7AM_to_8AM', (404, 154), (34, 21)), ('8AM_to_9AM', (479, 186), (41, 26)), ('8AM_to_9AM', (467, 179), (40, 25)), ('8AM_to_9AM', (460, 175), (39, 24)), ('9AM_to_10AM', (514, 221), (44, 31)), ('9AM_to_10AM', (490, 209), (41, 29)), ('10AM_to_11AM', (570, 286), (48, 40)), ('10AM_to_11AM', (564, 271), (48, 38)), ('10AM_to_11AM', (559, 262), (47, 37))]


import csv
import pandas as pd

# new_dict = {}
# for (key,point, value) in my_list:
#     if key in new_dict:
#
#         new_dict[key].append(point)
#         new_dict[key].append(value)
#     else:
#         new_dict[key] = [value]
# # print(new_dict)
df=pd.DataFrame(my_list,columns=["Time label","points","values"])


print(df)
# x11=new_dict['6AM_to_7AM'][0][0]
# y11=new_dict['6AM_to_7AM'][0][1]
# x21=new_dict['6AM_to_7AM'][1][0]
# y21=new_dict['6AM_to_7AM'][1][1]
# x12=new_dict['7AM_to_8AM'][0][0]
# y12=new_dict['7AM_to_8AM'][0][1]
# x22=new_dict['7AM_to_8AM'][1][0]
# y22=new_dict['7AM_to_8AM'][1][1]
# x13=new_dict['8AM_to_9AM'][0][0]
# y13=new_dict['8AM_to_9AM'][0][1]
# # print(x1)
# # print(y1)
# # print(x2)
# # print(y2)
# s1={'x1':x11,'y1':y11,'x2':x21,'y2':y21}
# s2={'x1':x12,'y1':y12,'x2':x22,'y2':y22}
# s3={'x1':x13,'y1':y13}
#
# print(s1)
#
# df=pd.DataFrame(columns=['x1','y1','x2','y2'])
# df=df.append([s1,s2,s3],ignore_index=True)
# df=df.rename(index={0:'6AM_to_7AM',1:'7AM_to_8AM',2:'8AM_to_9AM'})
# print(df)
df_csv=df.to_csv('data1.csv')
