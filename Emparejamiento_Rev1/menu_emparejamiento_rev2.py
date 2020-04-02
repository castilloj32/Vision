import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt



def menu_emparejamiento(emparejador,kp1,des1,kp2,des2,img1,img2):
#def menu_emparejamiento(emparejador):   
    if emparejador == 11:
        # BFMatcher with default params
        bf = cv.BFMatcher()
        matches = bf.knnMatch(des1,des2,k=2)
        # Apply ratio test
        good = []
        for m,n in matches:
            if m.distance < 0.75*n.distance:
                good.append([m])
        # cv.drawMatchesKnn expects list of lists as matches.
        img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        plt.imshow(img3),plt.show()

    if emparejador == 12:

        def flann1(valor):
            # FLANN parameters
            FLANN_INDEX_KDTREE = 1
            index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
            search_params = dict(checks=50)   # or pass empty dictionary
            flann = cv.FlannBasedMatcher(index_params,search_params)
            matches = flann.knnMatch(des1,des2,k=2)
            # Need to draw only good matches, so create a mask
            matchesMask = [[0,0] for i in range(len(matches))]
            # ratio test as per Lowe's paper
            
            ratio_thresh = 1
            for i,(m,n) in enumerate(matches):
                if m.distance < ratio_thresh*n.distance:
                    matchesMask[i]=[1,0]
            draw_params = dict(matchColor = (0,255,0),
                               singlePointColor = (255,0,0),
                               matchesMask = matchesMask,
                               flags = cv.DrawMatchesFlags_DEFAULT)
            img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
            plt.imshow(img3,),plt.show()
            title_trackbar="parametro"
            title_trackbar2="parametro2"
            window_name="Ventana1"
            cv.namedWindow(window_name)    
            cv.createTrackbar(title_trackbar, window_name , 0, 100, flann1)
            cv.imshow(window_name,img3)
            cv.waitKey()
    if emparejador == 13:
    
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
        for i,(m,n) in enumerate(matches):
            if m.distance < 0.7*n.distance:
                matchesMask[i]=[1,0]
        draw_params = dict(matchColor = (0,255,0),
                           singlePointColor = (255,0,0),
                           matchesMask = matchesMask,
                           flags = cv.DrawMatchesFlags_DEFAULT)
        img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
        plt.imshow(img3,),plt.show()
        
