import { Section, SectionNavWrap, SectionTitle, SectionTitleWrapSingle, SectionView } from '@/components/Section'
import { List, ListItem, ListTitle, ListCover, ListWrap, ListPrice, ListBuy } from '@/components/List'
import { IconPlus } from '@tabler/icons-react'

function GameItem() {
    return (
        <ListItem>
            <ListCover>
                <img src="https://picsum.photos/240/340" alt="" />
            </ListCover>

            <ListWrap>
                <ListTitle>
                    <a href="#">The Evil Within: The Assignment</a>
                </ListTitle>

                <ListPrice>
                    <span>$1.99</span>
                    <s>$4.99</s>
                    <b>60% OFF</b>
                </ListPrice>

                <ListBuy>
                    <IconPlus />
                </ListBuy>
            </ListWrap>
        </ListItem>
    )
}

export function OtherGames() {
    return (
        <Section>
            <div className="container">
                <div className="row">
                    <div className="col-12 col-md-6 col-xl-4">
                        <SectionTitleWrapSingle>
                            <SectionTitle small>Gaming Cards</SectionTitle>
                            <SectionNavWrap>
                                <SectionView>View All</SectionView>
                            </SectionNavWrap>
                        </SectionTitleWrapSingle>

                        <List>
                            <GameItem />
                            <GameItem />
                            <GameItem />
                        </List>
                    </div>

                    <div className="col-12 col-md-6 col-xl-4">
                        <SectionTitleWrapSingle>
                            <SectionTitle small>Gift Cards</SectionTitle>
                            <SectionNavWrap>
                                <SectionView>View All</SectionView>
                            </SectionNavWrap>
                        </SectionTitleWrapSingle>

                        <List>
                            <GameItem />
                            <GameItem />
                            <GameItem />
                        </List>
                    </div>

                    <div className="col-12 col-md-6 col-xl-4">
                        <SectionTitleWrapSingle>
                            <SectionTitle small>Subscriptions</SectionTitle>
                            <SectionNavWrap>
                                <SectionView>View All</SectionView>
                            </SectionNavWrap>
                        </SectionTitleWrapSingle>

                        <List>
                            <GameItem />
                            <GameItem />
                            <GameItem />
                        </List>
                    </div>
                </div>
            </div>
        </Section>
    )
}
