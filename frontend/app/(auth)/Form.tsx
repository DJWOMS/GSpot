import Link from 'next/link'
import Image from 'next/image'
import styled from 'styled-components'

export const SignContent = styled.div`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 100%;
    min-height: 100vh;
    padding: 40px 0;
`

export const SignForm = styled.form`
    background-color: #1b222e;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border: 1px solid rgba(167, 130, 233, 0.06);
    border-radius: 6px;
    padding: 40px 20px;
    position: relative;
    width: 100%;
    max-width: 400px;

    @media (min-width: 576px) {
        padding: 50px;
    }
`

export const SignLogo = styled(Link)`
    display: block;
    margin-bottom: 40px;
    transition: 0s;

    img {
        max-height: 80px;
    }

    @media (min-width: 576px) {
        margin-bottom: 50px;
    }
`

export const SignGroup = styled.div`
    position: relative;
    margin-bottom: 20px;
    width: 100%;
`

export const SignBtn = styled.button`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 44px;
    border-radius: 6px;
    background-color: #29b474;
    color: #fff;
    font-weight: 600;
    font-size: 13px;
    letter-spacing: 0.6px;
    margin-top: 15px;
    margin-bottom: 15px;
    text-transform: uppercase;

    :hover {
        background-color: #a782e9;
        color: #fff;
    }
`

export const SignDelimiter = styled.span`
    font-size: 13px;
    color: #dbdada;
    line-height: 100%;
`

export const SignInput = styled.input`
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

export const SignCheckbox = styled(SignGroup)`
    width: 100%;
    text-align: left;

    input:not(:checked),
    input:checked {
        position: absolute;
        left: -9999px;
    }

    input:not(:checked) + label,
    input:checked + label {
        font-size: 14px;
        color: #dbdada;
        font-weight: normal;
        position: relative;
        cursor: pointer;
        padding-left: 35px;
        line-height: 20px;
        margin: 0;
    }

    input:not(:checked) + label a,
    input:checked + label a {
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
        background: url('/img/checkmark.svg') no-repeat center/16px auto;
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
        color: #dbdada;
    }

    label::selection {
        background: transparent;
        color: #dbdada;
    }
`

export const SignText = styled.span`
    margin-top: 15px;
    font-size: 14px;
    color: #dbdada;

    a {
        position: relative;
        color: #a782e9;

        :hover {
            color: #a782e9;
            text-decoration: underline;
        }
    }
`

export const SignSocials = styled.div`
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-bottom: 15px;
    margin-top: 15px;
`

type ColorCodes<T extends string> = {
    [key in T]: string
} & { [key: string]: string }

const colors: ColorCodes<'fb' | 'gl' | 'tw'> = {
    fb: '#3b5999',
    gl: '#df4a32',
    tw: '#1da1f2',
}
interface SignSocialProps {
    color: 'fb' | 'gl' | 'tw'
}
export const SignSocial = styled.button<SignSocialProps>`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height: 44px;
    width: calc(33% - 10px);
    border-radius: 6px;

    background-color: ${(props) => colors[props.color]};

    svg {
        height: auto;
        stroke: #fff;
        transition: 0.5s ease;
        transition-property: stroke, fill;
    }

    :hover {
        background-color: #fff;

        svg {
            stroke: ${(props) => colors[props.color]};
        }
    }
`

interface FormProps {
    onSubmit: (data: object) => void
    children: React.ReactNode
}
export const Form = ({ onSubmit, children }: FormProps) => {
    return (
        <SignContent>
            <SignForm onSubmit={onSubmit}>
                <SignLogo href="/">
                    <Image width={496} height={161} src="/img/logo.png" alt="Logo" loading="eager" />
                </SignLogo>

                {children}
            </SignForm>
        </SignContent>
    )
}
