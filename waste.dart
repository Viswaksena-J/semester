import 'package:flutter/material.dart';
import 'package:test/core/app_export.dart';
import 'package:test/widgets/custom_search_view.dart';
import 'package:test/widgets/custom_text_form_field.dart';

// ignore_for_file: must_be_immutable
class VillageByLocationPage extends StatelessWidget {
  VillageByLocationPage({Key? key})
      : super(
          key: key,
        );

  TextEditingController searchController = TextEditingController();

  TextEditingController systemiconpxPlusController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    mediaQueryData = MediaQuery.of(context);

    return SafeArea(
      child: Scaffold(
        backgroundColor: appTheme.gray30001,
        resizeToAvoidBottomInset: false,
        body: Container(
          width: double.maxFinite,
          decoration: AppDecoration.fillGray,
          child: Column(
            children: [
              _buildThree(context),
              SizedBox(height: 15.v),
              Padding(
                padding: EdgeInsets.only(
                  left: 25.h,
                  right: 20.h,
                ),
                child: CustomTextFormField(
                  controller: systemiconpxPlusController,
                  hintText: "Add new shop",
                  textInputAction: TextInputAction.done,
                  suffix: Container(
                    margin: EdgeInsets.fromLTRB(30.h, 6.v, 5.h, 5.v),
                    child: CustomImageView(
                      imagePath: ImageConstant.imgSystemIcon24pxPlus,
                      height: 23.v,
                      width: 24.h,
                    ),
                  ),
                  suffixConstraints: BoxConstraints(
                    maxHeight: 35.v,
                  ),
                  contentPadding: EdgeInsets.only(
                    left: 20.h,
                    top: 5.v,
                    bottom: 5.v,
                  ),
                ),
              ),
              SizedBox(height: 5.v),
            ],
          ),
        ),
      ),
    );
  }

  /// Section Widget
  Widget _buildThree(BuildContext context) {
    return Container(
      padding: EdgeInsets.symmetric(horizontal: 13.h),
      decoration: AppDecoration.outlineBlack,
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Padding(
            padding: EdgeInsets.symmetric(horizontal: 3.h),
            child: CustomSearchView(
              controller: searchController,
              hintText: "Search for products",
            ),
          ),
          SizedBox(height: 2.v),
          Row(
            children: [
              CustomImageView(
                imagePath: ImageConstant.imgVector,
                height: 15.v,
                width: 10.h,
                margin: EdgeInsets.only(top: 1.v),
              ),
              Padding(
                padding: EdgeInsets.only(left: 6.h),
                child: Text(
                  "Srikalahasti",
                  style: CustomTextStyles.bodySmallAdaminaRed700,
                ),
              ),
            ],
          ),
          SizedBox(height: 8.v),
        ],
      ),
    );
  }
}
