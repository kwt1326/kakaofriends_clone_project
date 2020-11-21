import React from "react";
import HeadOfLists from "../../Components/HeadOfLists/headOfLists";
import HelpListTitle from "../../Components/Help_List/helpList";
import HelpListTitleBtn from "../../Components/Help_List/helpListTitleBtn";
import * as S from "./help_styles";

const Help = () => {
  return (
    <S.MainSection>
      <HeadOfLists title={"고객센터"} />
      <section>
        <HelpListTitleBtn />
        <ul>
          <HelpListTitle />
        </ul>
      </section>
    </S.MainSection>
  );
};

export default Help;
