'use client'

import { createGlobalStyle } from 'styled-components'

const GlobalStyles = createGlobalStyle`
    html {
        -webkit-text-size-adjust: 100%;
        -ms-text-size-adjust: 100%;
    }
    html,
    body {
        height: 100%;
    }
    body {
        font-family: 'Open Sans', sans-serif;
        font-weight: 400;
        -webkit-font-smoothing: antialiased;
        background-color: #1b222e;
    }
    button {
        padding: 0;
        border: none;
        background-color: transparent;
        transition: 0.5s ease;
        cursor: pointer;

        :focus {
            outline: none;
        }
    }
    a {
        transition: 0.5s ease;

        :hover,
        :active,
        :focus {
            outline: none;
            text-decoration: none;
        }
    }
    input,
    textarea,
    select {
        padding: 0;
        margin: 0;
        border-radius: 0;
        -webkit-appearance: none;
        -moz-appearance: none;
        -ms-appearance: none;
        appearance: none;
        box-shadow: none;
        transition: 0.5s ease;

        :focus {
            outline: none;
        }
    }
    select::-ms-expand {
        display: none;
    }
    ul {
        margin: 0;
        padding: 0;
        list-style: none;
    }
    ::-moz-selection {
        background: #a782e9;
        color: #fff;
        text-shadow: none;
    }
    ::selection {
        background: #a782e9;
        color: #fff;
        text-shadow: none;
    }
    ::-webkit-input-placeholder {
        color: #dbdada;
        opacity: 1;
    }
    ::-moz-placeholder {
        color: #dbdada;
        opacity: 1;
    }
    :-moz-placeholder {
        color: #dbdada;
        opacity: 1;
    }
    :-ms-input-placeholder {
        color: #dbdada;
        opacity: 1;
    }
    :focus {
        outline: -webkit-focus-ring-color auto 0px;
    }
        body::-webkit-scrollbar {
        width: 16px;
    }
        body::-webkit-scrollbar-track {
        background: rgba(167,130,233,0.06);
    }
        body::-webkit-scrollbar-thumb {
        background-color: #a782e9;
        outline: 1px solid rgba(167,130,233,0.06);
    }
    @media (min-width: 1310px) {
        .container {
            max-width: 1310px;
        }
    }
    .owl-carousel .owl-item img {
        width: auto;
        max-width: 100%;
    }
    .tab-content > .tab-pane {
        display: none;
    }
    .tab-content > .active {
        display: block;
    }
    .fade {
        transition: opacity 0.4s linear;

        :not(.show) {
            opacity: 0;
        }

        @media screen and (prefers-reduced-motion: reduce) {
            transition: none;
        }
    }
    .collapse:not(.show) {
        display: none;
    }
    .collapsing {
        position: relative;
        height: 0;
        overflow: hidden;
        transition: height 0.4s ease;

        @media screen and (prefers-reduced-motion: reduce) {
            transition: none;
        }
    }
    .table-responsive {
        display: block;
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        -ms-overflow-style: -ms-autohiding-scrollbar;
    }
    .table-responsive--border {
        border: 1px solid rgba(167,130,233,0.06);
        border-radius: 6px;
        margin-top: 30px;
    }
`

export default GlobalStyles
