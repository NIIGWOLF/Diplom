import sys, os
import shutil
def SilentMkdir(theDir):
    try:
        os.mkdir(theDir)
    except:
        pass
    return 0

def pars(str):
    arr = str.split()
    currentParam = ''
    strParam = ''
    dict = {}
    for x in range(1, len(arr)):
        if (re.match(r'--*', arr[x])):
            if (currentParam!=''):
                dict[currentParam] = [strParam.strip(),0]
            #print(currentParam+' '+ strParam.strip())
            currentParam = arr[x]
            strParam = ''
        else:
            strParam += ' ' + arr[x]
    #print(currentParam+' '+ strParam.strip())
    dict[currentParam] = [strParam.strip(), 0]
    node = Node(arr[0], arr[0], dict)
    return node

class Node:
    def __init__(self, name, run, dict):
        self.name = name
        self.run = run
        self.dict = dict

    def output(self):
        str = self.run
        for key in self.dict:
            str += ' ' + key + ' ' + self.dict.get(key)[0]
        return str


def Run_00_CameraInit(baseDir, aliceDir, srcImageDir):
    SilentMkdir(baseDir + "\\00_CameraInit")

    cmdLine =f'''{aliceDir}\\bin\\aliceVision_cameraInit.exe
        --defaultFieldOfView 45.0
        --verboseLevel info
        --allowSingleView 1
        --sensorDatabase "" 
        --imageFolder "{srcImageDir}"
        --output "{baseDir}\\00_CameraInit\\cameraInit.sfm"'''

    print(cmdLine.replace('\n',' '))
    os.system(cmdLine.replace('\n',' '))

    return 0


def Run_01_FeatureExtraction(baseDir, aliceDir, numImages):
    SilentMkdir(baseDir + "\\01_FeatureExtraction")

    cmdLine = f'''{aliceDir}\\bin\\aliceVision_featureExtraction.exe
        --input "{baseDir}\\00_CameraInit\\cameraInit.sfm"
        --describerTypes sift
        --describerPreset normal
        --forceCpuExtraction True
        --verboseLevel info
        --output {baseDir}\\01_FeatureExtraction
        --rangeStart 0
        --rangeSize {numImages}'''

    print(cmdLine.replace('\n',' '))
    os.system(cmdLine.replace('\n',' '))

    return 0


def Run_02_ImageMatching(baseDir, aliceDir):
    SilentMkdir(baseDir + "\\02_ImageMatching")

    cmdLine = f'''{aliceDir}\\bin\\aliceVision_imageMatching.exe
        --input "{baseDir}\\00_CameraInit\\cameraInit.sfm" 
        --featuresFolders "{baseDir}\\01_FeatureExtraction" 
        --tree "" 
        --weights "" 
        --minNbImages 200 
        --maxDescriptors 500 
        --nbMatches 50 
        --verboseLevel info 
        --output "{baseDir}\\02_ImageMatching\\imageMatches.txt"'''

    print(cmdLine.replace('\n', ' '))
    os.system(cmdLine.replace('\n', ' '))

    return 0


def Run_03_FeatureMatching(baseDir, aliceDir):
    SilentMkdir(baseDir + "\\03_FeatureMatching")

    cmdLine = f'''{aliceDir}\\bin\\aliceVision_featureMatching.exe
        --input "{baseDir}\\00_CameraInit\\cameraInit.sfm" 
        --featuresFolders "{baseDir}\\01_FeatureExtraction" 
        --imagePairsList "{baseDir}\\02_ImageMatching\\imageMatches.txt" 
        --describerTypes sift 
        --photometricMatchingMethod ANN_L2 
        --geometricEstimator acransac 
        --geometricFilterType fundamental_matrix 
        --distanceRatio 0.8 
        --maxIteration 2048 
        --geometricError 0.0 
        --maxMatches 0 
        --savePutativeMatches False 
        --guidedMatching False 
        --exportDebugFiles False 
        --verboseLevel info 
        --rangeStart 0 
        --rangeSize 20 
        --output "{baseDir}\\03_FeatureMatching"'''

    print(cmdLine.replace('\n', ' '))
    os.system(cmdLine.replace('\n', ' '))

    return 0


def Run_04_StructureFromMotion(baseDir, aliceDir):
    SilentMkdir(baseDir + "\\04_StructureFromMotion")

    cmdLine = f'''{aliceDir}\\bin\\aliceVision_incrementalSfm.exe
        --input "{baseDir}\\00_CameraInit\\cameraInit.sfm" 
        --featuresFolders "{baseDir}\\01_FeatureExtraction" 
        --matchesFolders "{baseDir}\\03_FeatureMatching" 
        --describerTypes sift 
        --localizerEstimator acransac 
        --localizerEstimatorMaxIterations 4096 
        --localizerEstimatorError 0.0 
        --lockScenePreviouslyReconstructed False 
        --useLocalBA True 
        --localBAGraphDistance 1 
        --maxNumberOfMatches 0 
        --minInputTrackLength 2 
        --minNumberOfObservationsForTriangulation 2 
        --minAngleForTriangulation 3.0 
        --minAngleForLandmark 2.0 
        --maxReprojectionError 4.0 
        --minAngleInitialPair 5.0 
        --maxAngleInitialPair 40.0 
        --useOnlyMatchesFromInputFolder False 
        --useRigConstraint True 
        --lockAllIntrinsics False 
        --initialPairA "" 
        --initialPairB "" 
        --interFileExtension .abc 
        --verboseLevel info 
        --outputViewsAndPoses "{baseDir}\\04_StructureFromMotion\\cameras.sfm" 
        --extraInfoFolder "{baseDir}\\04_StructureFromMotion"
        --output "{baseDir}\\04_StructureFromMotion\\sfm.abc"'''

    print(cmdLine.replace('\n', ' '))
    os.system(cmdLine.replace('\n', ' '))

    return 0


def Run_05_PrepareDenseScene(baseDir, aliceDir):
    SilentMkdir(baseDir + "\\05_PrepareDenseScene")

    cmdLine = f'''{aliceDir}\\bin\\aliceVision_prepareDenseScene.exe
        --input "{baseDir}\\04_StructureFromMotion\\sfm.abc"  
        --outputFileType exr 
        --saveMetadata True 
        --saveMatricesTxtFiles False 
        --evCorrection False 
        --verboseLevel info 
        --rangeStart 0 
        --rangeSize 40
        --output "{baseDir}\\05_PrepareDenseScene"'''

    print(cmdLine.replace('\n', ' '))
    os.system(cmdLine.replace('\n', ' '))
    return 0

def Run_06_DepthMap(baseDir, aliceDir, numImages, groupSize):
    SilentMkdir(baseDir + "\\06_DepthMap")

    cmdLine = f'''{aliceDir}\\bin\\aliceVision_depthMapEstimation.exe
        --input "{baseDir}\\04_StructureFromMotion\\sfm.abc"  
        --imagesFolder "{baseDir}\\05_PrepareDenseScene" 
        --downscale 2 
        --minViewAngle 2.0 
        --maxViewAngle 70.0 
        --sgmMaxTCams 10 
        --sgmWSH 4 
        --sgmGammaC 5.5 
        --sgmGammaP 8.0 
        --refineMaxTCams 6 
        --refineNSamplesHalf 150 
        --refineNDepthsToRefine 31 
        --refineNiters 100 
        --refineWSH 3 
        --refineSigma 15 
        --refineGammaC 15.5 
        --refineGammaP 8.0 
        --refineUseTcOrRcPixSize False 
        --exportIntermediateResults False 
        --nbGPUs 0 
        --verboseLevel info 
        --rangeStart 0 
        --rangeSize 3
        --output "{baseDir}\\06_DepthMap"'''

    print(cmdLine.replace('\n', ' '))
    os.system(cmdLine.replace('\n', ' '))

    cmdLine = f'''{aliceDir}\\bin\\aliceVision_depthMapEstimation.exe
            --input "{baseDir}\\04_StructureFromMotion\\sfm.abc"  
            --imagesFolder "{baseDir}\\05_PrepareDenseScene" 
            --downscale 2 
            --minViewAngle 2.0 
            --maxViewAngle 70.0 
            --sgmMaxTCams 10 
            --sgmWSH 4 
            --sgmGammaC 5.5 
            --sgmGammaP 8.0 
            --refineMaxTCams 6 
            --refineNSamplesHalf 150 
            --refineNDepthsToRefine 31 
            --refineNiters 100 
            --refineWSH 3 
            --refineSigma 15 
            --refineGammaC 15.5 
            --refineGammaP 8.0 
            --refineUseTcOrRcPixSize False 
            --exportIntermediateResults False 
            --nbGPUs 0 
            --verboseLevel info 
            --rangeStart 3 
            --rangeSize 3
            --output "{baseDir}\\06_DepthMap"'''

    print(cmdLine.replace('\n', ' '))
    os.system(cmdLine.replace('\n', ' '))

    return 0


def Run_07_DepthMapFilter(baseDir, aliceDir):
    SilentMkdir(baseDir + "\\07_DepthMapFilter")

    cmdLine = f'''{aliceDir}\\bin\\aliceVision_depthMapFiltering.exe
        --input "{baseDir}\\04_StructureFromMotion\\sfm.abc"  
        --depthMapsFolder "{baseDir}\\06_DepthMap" 
        --minViewAngle 2.0 
        --maxViewAngle 70.0 
        --nNearestCams 10 
        --minNumOfConsistentCams 3 
        --minNumOfConsistentCamsWithLowSimilarity 4 
        --pixSizeBall 0 
        --pixSizeBallWithLowSimilarity 0 
        --computeNormalMaps False 
        --verboseLevel info 
        --rangeStart 0 
        --rangeSize 10
        --output "{baseDir}\\07_DepthMapFilter"'''

    print(cmdLine.replace('\n', ' '))
    os.system(cmdLine.replace('\n', ' '))

    return 0


def Run_08_Meshing(baseDir, aliceDir):
    SilentMkdir(baseDir + "\\08_Meshing")

    cmdLine = f'''{aliceDir}\\bin\\aliceVision_meshing.exe
        --input "{baseDir}\\04_StructureFromMotion\\sfm.abc"  
        --depthMapsFolder "{baseDir}\\06_DepthMap" 
        --depthMapsFilterFolder "{baseDir}\\07_DepthMapFilter" 
        --estimateSpaceFromSfM True 
        --estimateSpaceMinObservations 3 
        --estimateSpaceMinObservationAngle 10 
        --maxInputPoints 50000000 
        --maxPoints 5000000 
        --maxPointsPerVoxel 1000000 
        --minStep 2 
        --partitioning singleBlock 
        --repartition multiResolution 
        --angleFactor 15.0 
        --simFactor 15.0 
        --pixSizeMarginInitCoef 2.0 
        --pixSizeMarginFinalCoef 4.0 
        --voteMarginFactor 4.0 
        --contributeMarginFactor 2.0 
        --simGaussianSizeInit 10.0 
        --simGaussianSize 10.0 
        --minAngleThreshold 1.0 
        --refineFuse True 
        --addLandmarksToTheDensePointCloud False 
        --colorizeOutput False 
        --saveRawDensePointCloud False 
        --verboseLevel info 
        --outputMesh "{baseDir}\\08_Meshing\\mesh.obj" 
        --output "{baseDir}\\08_Meshing\\densePointCloud.abc"'''

    print(cmdLine.replace('\n', ' '))
    os.system(cmdLine.replace('\n', ' '))

    return 0


def Run_09_MeshFiltering(baseDir, aliceDir):
    SilentMkdir(baseDir + "\\09_MeshFiltering")

    cmdLine = f'''{aliceDir}\\bin\\aliceVision_meshFiltering.exe
        --inputMesh "{baseDir}\\08_Meshing\\mesh.obj" 
        --keepLargestMeshOnly False 
        --iterations 5 
        --lambda 1.0 
        --verboseLevel info 
        --outputMesh "{baseDir}\\09_MeshFiltering\\mesh.obj"'''
    print(cmdLine.replace('\n', ' '))
    os.system(cmdLine.replace('\n', ' '))

    return 0


def Run_10_Texturing(baseDir, aliceDir):
    SilentMkdir(baseDir + "\\10_Texturing")

    cmdLine = f'''{aliceDir}\\bin\\aliceVision_texturing.exe
        --input "{baseDir}\\08_Meshing\\densePointCloud.abc" 
        --imagesFolder "{baseDir}\\05_PrepareDenseScene" 
        --inputMesh "{baseDir}\\09_MeshFiltering\\mesh.obj" 
        --textureSide 8192 
        --downscale 1 
        --outputTextureFileType png 
        --unwrapMethod Basic 
        --useUDIM True 
        --fillHoles False 
        --padding 5 
        --correctEV False 
        --useScore True 
        --processColorspace sRGB 
        --multiBandDownscale 4 
        --multiBandNbContrib 1 5 10 0 
        --bestScoreThreshold 0.1 
        --angleHardThreshold 90.0 
        --forceVisibleByAllVertices False 
        --flipNormals False 
        --visibilityRemappingMethod PullPush 
        --verboseLevel info 
        --output "{baseDir}\\10_Texturing"'''

    print(cmdLine.replace('\n', ' '))
    os.system(cmdLine.replace('\n', ' '))

    return 0