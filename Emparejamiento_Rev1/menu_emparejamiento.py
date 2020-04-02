import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt



def menu_emparejamiento(emparejador,kp1,des1,kp2,des2,img1,img2):
#def menu_emparejamiento(emparejador):   
    
    
    def slider_brute_force(val_slider):
        ratio_thresh=cv.getTrackbarPos(title_trackbar, window_name)
        kn_matches=cv.getTrackbarPos(title_trackbar2, window_name)
        brute_force(ratio_thresh,kn_matches)
    def slider_flann1(val_slider):
        ratio_thresh=cv.getTrackbarPos(title_trackbar, window_name)
        kn_matches=cv.getTrackbarPos(title_trackbar2, window_name)
        flann1(ratio_thresh,kn_matches)
    def slider_flann2(val_slider):
        ratio_thresh=cv.getTrackbarPos(title_trackbar, window_name)
        kn_matches=cv.getTrackbarPos(title_trackbar2, window_name)
        flann2(ratio_thresh,kn_matches)
        
    
        
        
    def brute_force(ratio_thresh,kn_matches):    
        
        ratio_thresh=ratio_thresh/10
    
        # BFMatcher with default params
        bf = cv.BFMatcher()
        #matches = bf.knnMatch(des1,des2,k=2)
        matches = bf.knnMatch(des1,des2,kn_matches)
        # Apply ratio test
        good = []
        for m,n in matches:
            #if m.distance < 0.75*n.distance:
            if m.distance < ratio_thresh*n.distance:
                good.append([m])
        # cv.drawMatchesKnn expects list of lists as matches.
        img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        #plt.imshow(img3),plt.show()
        img3 = cv.resize(img3,(1000,500))
        cv.imshow(window_name,img3)

    def flann1(ratio_thresh,kn_matches):
        
        ratio_thresh=ratio_thresh/10
        
        # FLANN parameters
        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks=50)   # or pass empty dictionary
        flann = cv.FlannBasedMatcher(index_params,search_params)
        matches = flann.knnMatch(des1,des2,kn_matches)
        #matches = flann.knnMatch(des1,des2,k=2)
        # Need to draw only good matches, so create a mask
        matchesMask = [[0,0] for i in range(len(matches))]
        # ratio test as per Lowe's paper
        
        #ratio_thresh = 1
        for i,(m,n) in enumerate(matches):
            if m.distance < ratio_thresh*n.distance:
                matchesMask[i]=[1,0]
        draw_params = dict(matchColor = (0,255,0),
                           singlePointColor = (255,0,0),
                           matchesMask = matchesMask,
                           flags = cv.DrawMatchesFlags_DEFAULT)
        img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
        #plt.imshow(img3,),plt.show()
        img3 = cv.resize(img3,(1000,500))
        cv.imshow(window_name,img3)
        
    def flann2(ratio_thresh,kn_matches):
        
        ratio_thresh=ratio_thresh/10
    
        FLANN_INDEX_KDTREE = 1
        FLANN_INDEX_LSH = 6
        index_params= dict(algorithm = FLANN_INDEX_LSH,
                       table_number = 6, # 12
                       key_size = 12,     # 20
                       multi_probe_level = 1) #2
        search_params = dict(checks=50)   # or pass empty dictionary
        flann = cv.FlannBasedMatcher(index_params,search_params)
        matches = flann.knnMatch(des1,des2,k=2)
        # Need to draw only good matches, so create a mask
        matchesMask = [[0,0] for i in range(len(matches))]
        # ratio test as per Lowe's paper
        #for i,(m,n) in enumerate(matches):
        for i,(m,n) in enumerate(matches):
            if m.distance < ratio_thresh*n.distance:
                matchesMask[i]=[1,0]
        draw_params = dict(matchColor = (0,255,0),
                           singlePointColor = (255,0,0),
                           matchesMask = matchesMask,
                           flags = cv.DrawMatchesFlags_DEFAULT)
        img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
        #plt.imshow(img3,),plt.show()
        img3 = cv.resize(img3,(1000,500))
        cv.imshow(window_name,img3)
        
    if emparejador == 11:
        title_trackbar="Lowe's radio test"
        title_trackbar2="Kn"
        window_name="Ventana1"
        cv.namedWindow(window_name)    
        cv.resizeWindow(window_name,500,400)
        cv.createTrackbar(title_trackbar, window_name , 0, 10, slider_brute_force)
        cv.createTrackbar(title_trackbar2, window_name , 2, 2, slider_brute_force)
        cv.waitKey()
        
    if emparejador == 13:
        title_trackbar="Lowe's radio test"
        title_trackbar2="Kn"
        window_name="Ventana1"
        cv.namedWindow(window_name)    
        cv.resizeWindow(window_name,500,400)
        cv.createTrackbar(title_trackbar, window_name , 0, 10, slider_flann1)
        cv.createTrackbar(title_trackbar2, window_name , 2, 2, slider_flann1)
        cv.waitKey()
        
    if emparejador == 12:
        title_trackbar="Lowe's radio test"
        title_trackbar2="Kn"
        window_name="Ventana1"
        cv.namedWindow(window_name)
        cv.resizeWindow(window_name,500,400)
        cv.createTrackbar(title_trackbar, window_name , 0, 10, slider_flann2)
        cv.createTrackbar(title_trackbar2, window_name , 2, 2, slider_flann2)
        cv.waitKey()
            
            