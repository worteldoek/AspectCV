import ctypes as ct
import io
import os
import numpy as np
import cv2

# To see documentation go to line

# TODO add other retrurn formats (succh as drawings on images etc)
# TODO add more descriptive errors
# TODO find out more what each parameter does


class MatchFailedException(Exception):
    pass


default_path = os.path.join(os.path.dirname(
    __file__), './build/x64/vc15/bin/MatchTool.dll')

dll_pattern_match = ct.WinDLL(default_path)

# initializing ctypes functions
_func_cpp_match = dll_pattern_match.Match
_func_cpp_match.restype = ct.c_bool

_func_cpp_set_source = dll_pattern_match.setSrc
_func_cpp_set_source.argtypes = np.ctypeslib.ndpointer(
    dtype=np.uint8, ndim=1, flags='C_CONTIGUOUS'), ct.c_int
_func_cpp_set_source.restype = None
_func_cpp_set_destination = dll_pattern_match.setDst
_func_cpp_set_destination.argtypes = np.ctypeslib.ndpointer(
    dtype=np.uint8, ndim=1, flags='C_CONTIGUOUS'), ct.c_int
_func_cpp_set_destination.restype = None

_func_cpp_set_minimum_reduced_area = dll_pattern_match.setMinReduceArea
_func_cpp_set_minimum_reduced_area.argtypes = [ct.c_int]
_func_cpp_set_minimum_reduced_area.restype = None

_func_cpp_toggle_bitwise_not = dll_pattern_match.setBitwiseNot
_func_cpp_toggle_bitwise_not.argtypes = [ct.c_bool]
_func_cpp_toggle_bitwise_not.restype = None

_func_cpp_toggle_tolerance_range = dll_pattern_match.setToleranceRange
_func_cpp_toggle_tolerance_range.argtypes = [ct.c_bool]
_func_cpp_toggle_tolerance_range.restype = None
_func_cpp_set_tolerance1 = dll_pattern_match.setTolerance1
_func_cpp_set_tolerance1.argtypes = [ct.c_double]
_func_cpp_set_tolerance1.restype = None
_func_cpp_set_tolerance2 = dll_pattern_match.setTolerance2
_func_cpp_set_tolerance2.argtypes = [ct.c_double]
_func_cpp_set_tolerance2.restype = None
_func_cpp_set_tolerance3 = dll_pattern_match.setTolerance3
_func_cpp_set_tolerance3.argtypes = [ct.c_double]
_func_cpp_set_tolerance3.restype = None
_func_cpp_set_tolerance4 = dll_pattern_match.setTolerance4
_func_cpp_set_tolerance4.argtypes = [ct.c_double]
_func_cpp_set_tolerance4.restype = None
_func_cpp_set_tolerance_angle = dll_pattern_match.setToleranceAngle
_func_cpp_set_tolerance_angle.argtypes = [ct.c_double]
_func_cpp_set_tolerance_angle.restype = None

_func_cpp_set_minimum_similarity_score = dll_pattern_match.setScore
_func_cpp_set_minimum_similarity_score.argtypes = [ct.c_double]
_func_cpp_set_minimum_similarity_score.restype = None

_func_cpp_toggle_SIMD = dll_pattern_match.setCkSIMD
_func_cpp_toggle_SIMD.argtypes = [ct.c_bool]
_func_cpp_toggle_SIMD.restype = None

_func_cpp_toggle_debug_mode = dll_pattern_match.setBDebugMode
_func_cpp_toggle_debug_mode.argtypes = [ct.c_bool]
_func_cpp_toggle_debug_mode.restype = None

_func_cpp_toggle_subpixel_estimation = dll_pattern_match.setBSubPixel
_func_cpp_toggle_subpixel_estimation.argtypes = [ct.c_bool]
_func_cpp_toggle_subpixel_estimation.restype = None

_func_cpp_set_maximum_overlap_ratio = dll_pattern_match.setMaxOverlap
_func_cpp_set_maximum_overlap_ratio.argtypes = [ct.c_double]
_func_cpp_set_maximum_overlap_ratio.restype = None

_func_cpp_set_number_of_targets = dll_pattern_match.setMaxPos
_func_cpp_set_number_of_targets.argtypes = [ct.c_int]
_func_cpp_set_number_of_targets.restype = None

_func_cpp_get_result_number_of_matches = dll_pattern_match.getResultSize
_func_cpp_get_result_number_of_matches.argtypes = []
_func_cpp_get_result_number_of_matches.restype = ct.c_int

_func_cpp_get_result_point_top_left_x = dll_pattern_match.resultGetAtIndexPointLeftTopX
_func_cpp_get_result_point_top_left_x.argtypes = [ct.c_int]
_func_cpp_get_result_point_top_left_x.restype = ct.c_double
_func_cpp_get_result_point_top_left_y = dll_pattern_match.resultGetAtIndexPointLeftTopY
_func_cpp_get_result_point_top_left_y.argtypes = [ct.c_int]
_func_cpp_get_result_point_top_left_y.restype = ct.c_double
_func_cpp_get_result_point_top_right_x = dll_pattern_match.resultGetAtIndexPointRightTopX
_func_cpp_get_result_point_top_right_x.argtypes = [ct.c_int]
_func_cpp_get_result_point_top_right_x.restype = ct.c_double
_func_cpp_get_result_point_top_right_y = dll_pattern_match.resultGetAtIndexPointRightTopY
_func_cpp_get_result_point_top_right_y.argtypes = [ct.c_int]
_func_cpp_get_result_point_top_right_y.restype = ct.c_double
_func_cpp_get_result_point_bot_right_x = dll_pattern_match.resultGetAtIndexPointRightBotX
_func_cpp_get_result_point_bot_right_x.argtypes = [ct.c_int]
_func_cpp_get_result_point_bot_right_x.restype = ct.c_double
_func_cpp_get_result_point_bot_right_y = dll_pattern_match.resultGetAtIndexPointRightBotY
_func_cpp_get_result_point_bot_right_y.argtypes = [ct.c_int]
_func_cpp_get_result_point_bot_right_y.restype = ct.c_double
_func_cpp_get_result_point_bot_left_x = dll_pattern_match.resultGetAtIndexPointLeftBotX
_func_cpp_get_result_point_bot_left_x.argtypes = [ct.c_int]
_func_cpp_get_result_point_bot_left_x.restype = ct.c_double
_func_cpp_get_result_point_bot_left_y = dll_pattern_match.resultGetAtIndexPointLeftBotY
_func_cpp_get_result_point_bot_left_y.argtypes = [ct.c_int]
_func_cpp_get_result_point_bot_left_y.restype = ct.c_double
_func_cpp_get_result_point_center_x = dll_pattern_match.resultGetAtIndexPointCenterX
_func_cpp_get_result_point_center_x.argtypes = [ct.c_int]
_func_cpp_get_result_point_center_x.restype = ct.c_double
_func_cpp_get_result_point_center_y = dll_pattern_match.resultGetAtIndexPointCenterY
_func_cpp_get_result_point_center_y.argtypes = [ct.c_int]
_func_cpp_get_result_point_center_y.restype = ct.c_double
_func_cpp_get_result_angle = dll_pattern_match.resultGetAtIndexMatchedAngle
_func_cpp_get_result_angle.argtypes = [ct.c_int]
_func_cpp_get_result_angle.restype = ct.c_double
_func_cpp_get_result_match_score = dll_pattern_match.resultGetAtIndexMatchScore
_func_cpp_get_result_match_score.argtypes = [ct.c_int]
_func_cpp_get_result_match_score.restype = ct.c_double


# bytes is the data after calling the .read() method on a buffered reader
# for more info on what the paramters do check the examples in: https://github.com/DennisLiu1993/Fastest_Image_Pattern_Matching
# using .bmp image is preferred, but other formats should also work
# finally, going beyond the specified parameter ranges below may lead to unexpected behaviour.
def matchFromImageBytes(
    # the source image (the image in which we search the pattern)
    source_image_bytes: bytes,
    destination_image_bytes: bytes,  # the destination image (the image)
    # the number of targets/matches expected to be found in the image.
    number_of_targets: int = 10,
    # (The algorithm will find this exact number of matches,
    #  however some will (probably) be filtered out due to not being percise enough)
    # allowed values are between
    # the minimum score value for each match (matches with lower score will be filtered out)
    min_similarity_score: float = 0.8,
    # values are between 0 and 0.8
    # the anlge at which a pattern may be rotated (values range from 0 to 180)
    tolerance_angle: float = 0,
    # how much overalpping is expected in the source image (values range from 0 to 0.8)
    overlap_ratio: float = 0,
    # enable SIMD mode (not sure what it stands for but this is commonly used for more complex images, see github for help)
    enable_SIMD: bool = False,
    # no idea what this is but the allowed values are between 64 and 2048
    minimum_reduced_area: int = 256,
    # enable doing subpixel estimation (probably useful for low-res images but I have not tested it)
    enable_subpixel_estimation: bool = False,
    # enbale checking the values between tolerance ranges (rarely used)
    enable_tolerance_ranges: bool = False,
    tolerance_range_1: float = 40,  # lower bound of first tolerance
    tolerance_range_2: float = 60,  # upper bound of first tolerance
    tolerance_range_3: float = -110,  # lower bound of second tolerance
    tolerance_range_4: float = -100,  # upper bound of second tolerance
    # no idea as well does not even show up in the gui of the main program
    enable_bitwise_not: bool = False,
    # enable debugging of the pattern match dll (useless parameter but still here to preserve complete functionality)
    enable_debug: bool = False,
) -> list[dict]:  # returns a list of dicts. Each dict contains information about a match
    # if the list is empty then there were no matches or there was an issue with the supplied parameters
    # the dict contians the following keys:
    # 'top_left_x' -> the x coordinate of the top left point in the match
    # 'top_left_y' -> the y coordinate of the top left point in the match
    # 'bot_left_x' -> the x coordinate of the bot left point in the match
    # 'bot_left_y' -> the y coordinate of the bot left point in the match
    # 'bot_right_x' -> the x coordinate of the bot right point in the match
    # 'bot_right_y' -> the y coordinate of the bot right point in the match
    # 'bot_left_x' -> the x coordinate of the bot left point in the match
    # 'bot_left_y' -> the y coordinate of the bot left point in the match
    # 'center_x' -> the x coordinate of the center point in the match
    # 'center_y' -> the x coordinate of the center point in the match
    # 'angle' -> the angle at which the match is rotated
    # 'score' -> how close(similar) the match is to the destination image

    # loading images
    # creating np array form bytes buffer with proper fromat so c++ code can read it easily
    source_image_bytes_np_arr = np.frombuffer(source_image_bytes, np.uint8)
    # finding the size of the arr so we allocate enough memory for the vector in c++
    source_image_bytes_np_arr_size = source_image_bytes_np_arr.shape[0]
    _func_cpp_set_source(
        source_image_bytes_np_arr, source_image_bytes_np_arr_size)

    destination_image_bytes_np_arr = np.frombuffer(
        destination_image_bytes, np.uint8)
    destination_image_bytes_np_arr_size = destination_image_bytes_np_arr.shape[0]
    _func_cpp_set_destination(
        destination_image_bytes_np_arr, destination_image_bytes_np_arr_size)

    # passing params onto the c++ library
    _func_cpp_set_minimum_reduced_area(ct.c_int(minimum_reduced_area))
    _func_cpp_toggle_bitwise_not(ct.c_bool(enable_bitwise_not))
    _func_cpp_toggle_tolerance_range(
        ct.c_bool(enable_tolerance_ranges))
    _func_cpp_set_tolerance1(ct.c_double(tolerance_range_1))
    _func_cpp_set_tolerance2(ct.c_double(tolerance_range_2))
    _func_cpp_set_tolerance3(ct.c_double(tolerance_range_3))
    _func_cpp_set_tolerance4(ct.c_double(tolerance_range_4))
    _func_cpp_set_tolerance_angle(ct.c_double(tolerance_angle))
    _func_cpp_set_minimum_similarity_score(
        ct.c_double(min_similarity_score))
    _func_cpp_toggle_SIMD(ct.c_bool(enable_SIMD))
    _func_cpp_toggle_debug_mode(ct.c_bool(enable_debug))
    _func_cpp_toggle_subpixel_estimation(
        ct.c_bool(enable_subpixel_estimation))
    _func_cpp_set_maximum_overlap_ratio(ct.c_double(overlap_ratio))
    _func_cpp_set_number_of_targets(ct.c_int(number_of_targets))

    # ------MATCHING------#
    success = _func_cpp_match()
    # --------------------#
    if not success:
        "Could not find any targets. Or parameters are incorrect."
        return []
    # rebuilding the results
    result_list = []

    result_lenght = _func_cpp_get_result_number_of_matches()
    print(result_lenght)
    for i in range(result_lenght):
        single_match = {}
        single_match['top_left_x'] = _func_cpp_get_result_point_top_left_x(
            ct.c_int(i))
        single_match['top_left_y'] = _func_cpp_get_result_point_top_left_y(
            ct.c_int(i))
        single_match['bot_left_x'] = _func_cpp_get_result_point_bot_left_x(
            ct.c_int(i))
        single_match['bot_left_y'] = _func_cpp_get_result_point_bot_left_y(
            ct.c_int(i))
        single_match['bot_right_x'] = _func_cpp_get_result_point_bot_right_x(
            ct.c_int(i))
        single_match['bot_right_y'] = _func_cpp_get_result_point_bot_right_y(
            ct.c_int(i))
        single_match['top_right_x'] = _func_cpp_get_result_point_top_right_x(
            ct.c_int(i))
        single_match['top_right_y'] = _func_cpp_get_result_point_top_right_y(
            ct.c_int(i))
        single_match['center_x'] = _func_cpp_get_result_point_center_x(
            ct.c_int(i))
        single_match['center_y'] = _func_cpp_get_result_point_center_y(
            ct.c_int(i))
        single_match['angle'] = _func_cpp_get_result_angle(
            ct.c_int(i))
        single_match['score'] = _func_cpp_get_result_match_score(
            ct.c_int(i))
        result_list.append(single_match)

    return result_list
# load image from file path
# see match image from bytes for fuller documention
def matchFromImagePath(
    # the sourve image (the image in which we search the pattern)
    source_image_path: str,
    destination_image_path: str,  # the destination image (the image)
    # the number of targets/matches expected to be found in the image.
    number_of_targets: int = 10,
    # (The algorithm will find this exact number of matches,
    #  however some will (probably) be filtered out due to not being percise enough)
    # allowed values are between
    # the minimum score value for each match (matches with lower score will be filtered out)
    min_similarity_score: float = 0.8,
    # values are between 0 and 0.8
    # the anlge at which a pattern may be rotated (values range from 0 to 180)
    tolerance_angle: float = 0,
    # how much overalpping is expected in the source image (values range from 0 to 0.8)
    overlap_ratio: float = 0,
    # enable SIMD mode (not sure what it stands for but this is commonly used for more complex images, see github for help)
    enable_SIMD: bool = False,
    # no idea what this is but the allowed values are between 64 and 2048
    minimum_reduced_area: int = 256,
    # enable doing subpixel estimation (probably useful for low-res images but I have not tested it)
    enable_subpixel_estimation: bool = False,
    # enbale checking the values between tolerance ranges (rarely used)
    enable_tolerance_ranges: bool = False,
    tolerance_range_1: float = 40,  # lower bound of first tolerance
    tolerance_range_2: float = 60,  # upper bound of first tolerance
    tolerance_range_3: float = -110,  # lower bound of second tolerance
    tolerance_range_4: float = -100,  # upper bound of second tolerance
    # no idea as well does not even show up in the gui of the main program
    enable_bitwise_not: bool = False,
    # enable debugging of the pattern match dll (useless parameter but still here to preserve complete functionality)
    enable_debug: bool = False,
) -> None:  # returns a list of dicts. Each dict contains information about a match
    # the dict contians the following keys:
    # 'top_left_x' -> the x coordinate of the top left point in the match
    # 'top_left_y' -> the y coordinate of the top left point in the match
    # 'bot_left_x' -> the x coordinate of the bot left point in the match
    # 'bot_left_y' -> the y coordinate of the bot left point in the match
    # 'bot_right_x' -> the x coordinate of the bot right point in the match
    # 'bot_right_y' -> the y coordinate of the bot right point in the match
    # 'bot_left_x' -> the x coordinate of the bot left point in the match
    # 'bot_left_y' -> the y coordinate of the bot left point in the match
    # 'center_x' -> the x coordinate of the center point in the match
    # 'center_y' -> the x coordinate of the center point in the match
    # 'angle' -> the angle at which the match is rotated
    # 'score' -> how close(similar) the match is to the destination image

    with open(source_image_path, 'rb') as source_reader:
        source_image_bytes = source_reader.read()
    with open(destination_image_path, 'rb') as destination_reader:
        destination_image_bytes = destination_reader.read()
    
    return matchFromImageBytes(
        source_image_bytes,
        destination_image_bytes,
        number_of_targets,
        min_similarity_score,
        tolerance_angle,
        overlap_ratio,
        enable_SIMD,
        minimum_reduced_area,
        enable_subpixel_estimation,
        enable_tolerance_ranges,
        tolerance_range_1,
        tolerance_range_2,
        tolerance_range_3,
        tolerance_range_4,
        enable_bitwise_not,
        enable_debug,
    )

# load image from opencv image
# If you see the typehint actually opencv images are numpy arrays
# see match image from bytes for fuller documention
def matchFromImageCV2(
    # the sourve image (the image in which we search the pattern)
    source_image_cv2: np.ndarray,
    destination_image_cv2: np.ndarray,  # the destination image (the image for which we search)
    # the number of targets/matches expected to be found in the image.
    number_of_targets: int = 10,
    # (The algorithm will find this exact number of matches,
    #  however some will (probably) be filtered out due to not being percise enough)
    # allowed values are between
    # the minimum score value for each match (matches with lower score will be filtered out)
    min_similarity_score: float = 0.8,
    # values are between 0 and 0.8
    # the anlge at which a pattern may be rotated (values range from 0 to 180)
    tolerance_angle: float = 0,
    # how much overalpping is expected in the source image (values range from 0 to 0.8)
    overlap_ratio: float = 0,
    # enable SIMD mode (not sure what it stands for but this is commonly used for more complex images, see github for help)
    enable_SIMD: bool = False,
    # no idea what this is but the allowed values are between 64 and 2048
    minimum_reduced_area: int = 256,
    # enable doing subpixel estimation (probably useful for low-res images but I have not tested it)
    enable_subpixel_estimation: bool = False,
    # enbale checking the values between tolerance ranges (rarely used)
    enable_tolerance_ranges: bool = False,
    tolerance_range_1: float = 40,  # lower bound of first tolerance
    tolerance_range_2: float = 60,  # upper bound of first tolerance
    tolerance_range_3: float = -110,  # lower bound of second tolerance
    tolerance_range_4: float = -100,  # upper bound of second tolerance
    # no idea as well does not even show up in the gui of the main program
    enable_bitwise_not: bool = False,
    # enable debugging of the pattern match dll (useless parameter but still here to preserve complete functionality)
    enable_debug: bool = False,
) -> None:  # returns a list of dicts. Each dict contains information about a match
    # the dict contians the following keys:
    # 'top_left_x' -> the x coordinate of the top left point in the match
    # 'top_left_y' -> the y coordinate of the top left point in the match
    # 'bot_left_x' -> the x coordinate of the bot left point in the match
    # 'bot_left_y' -> the y coordinate of the bot left point in the match
    # 'bot_right_x' -> the x coordinate of the bot right point in the match
    # 'bot_right_y' -> the y coordinate of the bot right point in the match
    # 'bot_left_x' -> the x coordinate of the bot left point in the match
    # 'bot_left_y' -> the y coordinate of the bot left point in the match
    # 'center_x' -> the x coordinate of the center point in the match
    # 'center_y' -> the x coordinate of the center point in the match
    # 'angle' -> the angle at which the match is rotated
    # 'score' -> how close(similar) the match is to the destination image

    source_image_bytes: bytes = cv2.imencode(".jpg", source_image_cv2)[1].tobytes()
    destination_image_bytes: bytes = cv2.imencode(".jpg", destination_image_cv2)[1].tobytes()
    
    return matchFromImageBytes(
        source_image_bytes,
        destination_image_bytes,
        number_of_targets,
        min_similarity_score,
        tolerance_angle,
        overlap_ratio,
        enable_SIMD,
        minimum_reduced_area,
        enable_subpixel_estimation,
        enable_tolerance_ranges,
        tolerance_range_1,
        tolerance_range_2,
        tolerance_range_3,
        tolerance_range_4,
        enable_bitwise_not,
        enable_debug,
    )

if __name__ == '__main__':

    source_path = "python/testImages/Src1.bmp"
    destination_path = "python/testImages/20220611.bmp"
    result = matchFromImagePath(
        source_image_path=source_path,
        destination_image_path=destination_path,
        tolerance_angle=180,
        min_similarity_score=0.7
    )
    for d in result:
        print(d['center_x'], d['center_y'], d['angle'], d['score'])
        source_path = "Src1.bmp"
    assert (len(result) == 7)

    print('--------------')
    source_path = "python/testImages/Src9.bmp"
    destination_path = "python/testImages/Dst9.bmp"
    result = matchFromImagePath(
        source_image_path=source_path,
        destination_image_path=destination_path,
        number_of_targets=7,
        tolerance_angle=180,
        min_similarity_score=0.7,
        overlap_ratio=0.7,
        enable_SIMD=True,
    )
    for d in result:
        print(d['center_x'], d['center_y'], d['angle'], d['score'])

    assert (len(result) == 4)

    print('--------------')

    source_path = "python/testImages/Src6.jpg"
    destination_path = "python/testImages/Dst6.bmp"
    result = matchFromImagePath(
        source_image_path=source_path,
        destination_image_path=destination_path,
        number_of_targets=15,
        tolerance_angle=180,
        min_similarity_score=0.8,
        enable_SIMD=True,
    )
    for d in result:
        print(d['center_x'], d['center_y'], d['angle'], d['score'])

    assert (len(result) == 15)

    # print(result)
