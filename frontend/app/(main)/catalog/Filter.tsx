'use client'

import styled from 'styled-components'

const OpenFilter = styled.button`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 44px;
    background-color: rgba(167, 130, 233, 0.03);
    border: 1px solid rgba(167, 130, 233, 0.4);
    border-radius: 6px;
    font-size: 12px;
    color: #fff;
    letter-spacing: 0.4px;
    text-transform: uppercase;
    margin-bottom: 10px;

    :hover {
        background-color: rgba(167, 130, 233, 0.04);
        border-color: rgba(167, 130, 233, 0.5);

        svg {
            stroke: #a782e9;
        }
    }

    @media (min-width: 576px) {
        margin-bottom: 20px;
    }
    @media (min-width: 992px) {
        display: none;
    }
`

const StyledComponents = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    margin-bottom: 10px;
    margin-top: 20px;

    @media (min-width: 576px) {
        margin-bottom: 20px;
    }
    @media (min-width: 992px) {
        margin-top: 30px;
    }
    @media (min-width: 1310px) {
        padding-right: 10px;
    }
`

const WrapContent = styled.div`
    @media (min-width: 992px) {
        display: block !important;
    }
`

const Title = styled.h4`
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    height: auto;
    width: 100%;
    color: #fff;
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 25px;
    letter-spacing: 0.4px;
`

const ClearFilter = styled.button`
    font-size: 12px;
    font-weight: 400;
    color: #a782e9;
    letter-spacing: 0;

    :hover {
        color: #fd6060;
    }
`

const Group = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    width: 100%;
    margin-bottom: 30px;

    :last-child {
        margin-bottom: 0;
    }
`

const Label = styled.label`
    font-size: 14px;
    line-height: 100%;
    letter-spacing: 0.4px;
    color: #dbdada;
    font-weight: normal;
    margin-bottom: 15px;
`

const SelectWrap = styled.div`
    position: relative;
    width: 100%;
`

const Select = styled.select`
    width: 100%;
    height: 44px;
    border-radius: 6px;
    border: 1px solid rgba(167, 130, 233, 0.06);
    font-size: 14px;
    color: #fff;
    padding: 0 20px;
    cursor: pointer;
    background: url('/img/arrow2.svg') no-repeat center right 20px rgba(167, 130, 233, 0.03);
    background-size: 12px auto;
    letter-spacing: 0.4px;

    option {
        padding: 0;
        margin: 0;
        color: #000;
    }

    :focus {
        background-color: rgba(167, 130, 233, 0.04);
        border-color: rgba(167, 130, 233, 0.5);
    }
`

const Input = styled.input`
    background-color: rgba(167, 130, 233, 0.03);
    border: 1px solid rgba(167, 130, 233, 0.06);
    border-radius: 6px;
    height: 44px;
    position: relative;
    color: #fff;
    font-size: 14px;
    width: 100%;
    padding: 0 20px;
    letter-spacing: 0.4px;

    :focus {
        background-color: rgba(167, 130, 233, 0.04);
        border-color: rgba(167, 130, 233, 0.5);
    }
`

const Checkboxes = styled.ul`
    position: relative;
    margin-top: 5px;
`

const Checkbox = styled.li`
    position: relative;
    margin-bottom: 15px;

    :last-child {
        margin-bottom: 0;
    }

    input:not(:checked),
    input:checked {
        position: absolute;
        left: -9999px;
    }

    input:not(:checked) + label,
    input:checked + label {
        font-size: 14px;
        color: #fff;
        font-weight: normal;
        position: relative;
        cursor: pointer;
        padding-left: 35px;
        line-height: 20px;
        letter-spacing: 0.4px;
        margin: 0;
    }

    input:not(:checked) + label a,
    input:checked + label a {
        color: #a782e9;
    }

    input:not(:checked) + label a:hover,
    input:checked + label a:hover {
        color: #a782e9;
    }

    input:not(:checked) + label:before,
    input:checked + label:before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        width: 20px;
        height: 20px;
        background-color: rgba(167, 130, 233, 0.03);
        border: 1px solid rgba(167, 130, 233, 0.06);
        border-radius: 6px;
    }

    input:not(:checked) + label:after,
    input:checked + label:after {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        width: 20px;
        height: 20px;
        text-align: center;
        transition: 0.5s;
        background: url('../img/checkmark.svg') no-repeat center/16px auto;
    }

    input:not(:checked) + label:after {
        opacity: 0;
        transform: scale(0);
    }

    input:checked + label:after {
        opacity: 1;
        transform: scale(1);
    }

    label::-moz-selection {
        background: transparent;
        color: #fff;
    }

    label::selection {
        background: transparent;
        color: #fff;
    }
`

const Range = styled.div`
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    background-color: rgba(167, 130, 233, 0.03);
    border: 1px solid rgba(167, 130, 233, 0.06);
    font-size: 13px;
    color: #fff;
    position: relative;
    margin-bottom: 10px;
    height: 30px;
    padding: 0 12px;
    border-radius: 6px;
    letter-spacing: 0.4px;

    div {
        position: relative;

        :first-child {
            margin-right: 16px;

            :after {
                content: '–';
                position: absolute;
                display: block;
                left: 100%;
                top: 0;
                color: #fff;
                font-size: 14px;
                margin-left: 4px;
                line-height: 16px;
            }
        }
    }
`

const ApplyFilter = styled.button`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 44px;
    background-color: rgba(167, 130, 233, 0.03);
    border: 1px solid rgba(167, 130, 233, 0.4);
    border-radius: 6px;
    font-size: 12px;
    color: #fff;
    letter-spacing: 0.4px;
    text-transform: uppercase;

    :hover {
        background-color: rgba(167, 130, 233, 0.04);
        border-color: rgba(167, 130, 233, 0.5);
    }

    :hover svg {
        stroke: #a782e9;
    }
`

export function Filter() {
    return (
        <div className="filter-wrap">
            <OpenFilter>Открыть фильтр</OpenFilter>

            <WrapContent>
                <StyledComponents>
                    <Title>
                        Фильтры <ClearFilter>Очистить</ClearFilter>
                    </Title>

                    <Group>
                        <Label>Ключевые слова: </Label>
                        <Input type="text" placeholder="Keyword" />
                    </Group>

                    <Group>
                        <Label>Сортировать: </Label>

                        <SelectWrap>
                            <Select>
                                <option value="0">По интересам</option>
                                <option value="1">От новых к старым</option>
                                <option value="2">От старых к новым</option>
                            </Select>
                        </SelectWrap>
                    </Group>

                    <Group>
                        <Label>Цена: </Label>

                        <Range>
                            <div id="filter__range-start"></div>
                            <div id="filter__range-end"></div>
                        </Range>

                        <Range />
                    </Group>

                    <Group>
                        <Label>Платформа: </Label>
                        <Checkboxes>
                            <Checkbox>
                                <input id="type1" type="checkbox" name="type1" checked />
                                <label htmlFor="type1">Playstation</label>
                            </Checkbox>
                            <Checkbox>
                                <input id="type2" type="checkbox" name="type2" />
                                <label htmlFor="type2">XBOX</label>
                            </Checkbox>
                            <Checkbox>
                                <input id="type3" type="checkbox" name="type3" />
                                <label htmlFor="type3">Windows</label>
                            </Checkbox>
                            <Checkbox>
                                <input id="type4" type="checkbox" name="type4" />
                                <label htmlFor="type4">Mac OS</label>
                            </Checkbox>
                        </Checkboxes>
                    </Group>

                    <Group>
                        <Label>Жанры:</Label>
                        <Checkboxes>
                            <Checkbox>
                                <input id="type5" type="checkbox" name="type5" checked />
                                <label htmlFor="type5">Action</label>
                            </Checkbox>
                            <Checkbox>
                                <input id="type6" type="checkbox" name="type6" />
                                <label htmlFor="type6">Adventure</label>
                            </Checkbox>
                            <Checkbox>
                                <input id="type7" type="checkbox" name="type7" checked />
                                <label htmlFor="type7">Fighting</label>
                            </Checkbox>
                            <Checkbox>
                                <input id="type8" type="checkbox" name="type8" checked />
                                <label htmlFor="type8">Flight simulation</label>
                            </Checkbox>
                            <Checkbox>
                                <input id="type9" type="checkbox" name="type9" />
                                <label htmlFor="type9">Platform</label>
                            </Checkbox>
                            <Checkbox>
                                <input id="type10" type="checkbox" name="type10" />
                                <label htmlFor="type10">Racing</label>
                            </Checkbox>
                            <Checkbox>
                                <input id="type11" type="checkbox" name="type11" />
                                <label htmlFor="type11">RPG</label>
                            </Checkbox>
                            <Checkbox>
                                <input id="type12" type="checkbox" name="type12" />
                                <label htmlFor="type12">Sports</label>
                            </Checkbox>
                            <Checkbox>
                                <input id="type13" type="checkbox" name="type13" />
                                <label htmlFor="type13">Strategy</label>
                            </Checkbox>
                            <Checkbox>
                                <input id="type14" type="checkbox" name="type14" />
                                <label htmlFor="type14">Survival horror</label>
                            </Checkbox>
                        </Checkboxes>
                    </Group>

                    <Group>
                        <ApplyFilter>Применить фильтр</ApplyFilter>
                    </Group>
                </StyledComponents>
            </WrapContent>
        </div>
    )
}
