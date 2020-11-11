import styled from "@emotion/styled";

export const HomeWarp = styled.div`
  .my-masonry-grid {
    display: -webkit-box; /* Not needed if autoprefixing */
    display: -ms-flexbox; /* Not needed if autoprefixing */
    display: flex;
    margin-left: -30px; /* gutter size offset */
    width: auto;
  }
  .my-masonry-grid_column {
    /* padding-left: 30px; gutter size */
    background-clip: padding-box;
  }

  /* Style your items */
  .my-masonry-grid_column > div {
    /* change div to reference your elements you put in <Masonry> */
    background: grey;
    margin-bottom: 30px;
  }
`;

export const ItemWrap = styled.article`
  background-image: none;
  border-bottom: 0px;

  padding: 0px 23px 40px;

  & > div {
    border-radius: 6px;
    box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 13px;
  }
`;

export const Description = styled.div`
  padding: 20px 20px 30px;
`;

export const Img = styled.img`
  width: 100%;
`;
